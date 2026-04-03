from __future__ import annotations

import asyncio
import json
import logging
import time
from collections.abc import AsyncIterator

from fastapi import APIRouter, Depends, File, Form, Request, UploadFile
from fastapi.responses import Response, StreamingResponse
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from aether_runner.core.auth import auth_dependency
from aether_runner.core.config import Settings
from aether_runner.core.errors import RunnerError
from aether_runner.core.metrics import MODEL_LATENCY, PREPROCESS_LATENCY, REQUEST_COUNT, REQUEST_LATENCY
from aether_runner.models.schemas import (
    ChatChoice,
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChoiceMessage,
    HealthResponse,
    LegacyCompletionRequest,
    MMParseResponse,
    MediaIngestResponse,
    ModelListItem,
    ModelListResponse,
    ResponseOutputText,
    ResponsesRequest,
    ResponsesResponse,
    SpeechRequest,
    TranslationRequest,
    TranscriptionRequest,
    Usage,
    VideoUnderstandRequest,
    VideoUnderstandResponse,
)
from aether_runner.services.executor import RunnerExecutor
from aether_runner.services.media_ingest import MediaIngestService
from aether_runner.services.model_registry import ModelRegistry
from aether_runner.services.normalization import from_chat_request, from_completion_request, from_responses_request

logger = logging.getLogger(__name__)


def _sse_pack(data: dict) -> str:
    return f"data: {json.dumps(data)}\n\n"


async def _stream_chat(iterator) -> AsyncIterator[str]:
    for delta in iterator:
        payload = {
            "object": "chat.completion.chunk",
            "choices": [{"index": 0, "delta": {"content": delta.get("delta", "")}, "finish_reason": None}],
        }
        yield _sse_pack(payload)
        await asyncio.sleep(0)
    yield _sse_pack({"choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]})
    yield "data: [DONE]\n\n"


async def _stream_responses(iterator) -> AsyncIterator[str]:
    for delta in iterator:
        payload = {"type": "response.output_text.delta", "delta": delta.get("delta", "")}
        yield _sse_pack(payload)
        await asyncio.sleep(0)
    yield _sse_pack({"type": "response.completed"})
    yield "data: [DONE]\n\n"


def build_router(settings: Settings, registry: ModelRegistry, ingest: MediaIngestService, executor: RunnerExecutor) -> APIRouter:
    router = APIRouter(dependencies=[auth_dependency(settings)])

    @router.get("/healthz", response_model=HealthResponse)
    def healthz() -> HealthResponse:
        return HealthResponse(status="ok", detail={"service": "aether-runner"})

    @router.get("/livez", response_model=HealthResponse)
    def livez() -> HealthResponse:
        return HealthResponse(status="ok", detail={"service": "aether-runner"})

    @router.get("/readyz", response_model=HealthResponse)
    def readyz() -> HealthResponse:
        if registry.ready():
            return HealthResponse(status="ok", detail={"models": len(registry.list_manifests())})
        return HealthResponse(status="not_ready", detail={"reason": "model registry not loaded"})

    @router.get("/metrics")
    def metrics() -> Response:
        return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

    @router.get("/aether/v1/capabilities")
    def capabilities() -> dict:
        return {"object": "list", "data": [m.model_dump() for m in registry.list_manifests()]}

    @router.get("/v1/models", response_model=ModelListResponse)
    def v1_models() -> ModelListResponse:
        items = [ModelListItem(id=m.id, capabilities=m) for m in registry.list_manifests()]
        return ModelListResponse(data=items)

    @router.get("/aether/v1/assets/{asset_id}")
    def asset_meta(asset_id: str) -> dict:
        asset = ingest.registry.maybe_get(asset_id)
        if not asset:
            raise RunnerError("asset_not_found", f"Asset '{asset_id}' not found.", status_code=404)
        return {"asset": asset.model_dump()}

    @router.post("/aether/v1/media/ingest", response_model=MediaIngestResponse)
    async def media_ingest(
        file: UploadFile | None = File(default=None),
        base64_data: str | None = Form(default=None),
        local_path: str | None = Form(default=None),
        url: str | None = Form(default=None),
    ) -> MediaIngestResponse:
        if file is not None:
            payload = await file.read()
            asset = ingest.ingest_upload(file.filename or "upload.bin", payload)
            return MediaIngestResponse(asset=asset)
        if base64_data:
            return MediaIngestResponse(asset=ingest.ingest_base64(base64_data))
        if local_path:
            return MediaIngestResponse(asset=ingest.ingest_path(local_path))
        if url:
            return MediaIngestResponse(asset=ingest.ingest_url(url))
        raise RunnerError("asset_ingest_failed", "Provide one of file, base64_data, local_path, or url.", status_code=400)

    @router.post("/aether/v1/mm/parse", response_model=MMParseResponse)
    def mm_parse(req: ChatCompletionRequest) -> MMParseResponse:
        canonical = from_chat_request(req)
        model = registry.get(canonical.model)
        _, prep = executor.prepare(canonical, model)
        return MMParseResponse(
            request_id=canonical.request_id,
            model=canonical.model,
            route=canonical.route,
            modalities=sorted(canonical.modalities()),
            token_estimate=prep.token_estimate,
            assets=prep.assets,
            plan=prep.plan,
        )

    @router.post("/aether/v1/video/understand", response_model=VideoUnderstandResponse)
    def video_understand(req: VideoUnderstandRequest) -> VideoUnderstandResponse:
        model = registry.get(req.model)
        if not model.manifest.supports_video_frames:
            raise RunnerError("unsupported_route", "Model does not support video frames.", status_code=400)
        if not req.asset_id:
            raise RunnerError("asset_ingest_failed", "asset_id is required for video understand.", status_code=400)
        asset = ingest.registry.maybe_get(req.asset_id)
        if not asset:
            raise RunnerError("asset_not_found", f"Asset '{req.asset_id}' not found.", status_code=404)
        summary = f"Video analysis queued for {asset.asset_id}; integrate frame extraction backend for full output."
        return VideoUnderstandResponse(
            model=req.model,
            summary=summary,
            scene_events=[],
        )

    @router.post("/v1/chat/completions", response_model=ChatCompletionResponse)
    async def chat_completions(req: ChatCompletionRequest, request: Request):
        started = time.perf_counter()
        canonical = from_chat_request(req)
        model = registry.get(canonical.model)

        if req.stream:
            stream, prep = executor.stream_generate(canonical, model)
            PREPROCESS_LATENCY.labels(route=canonical.route).observe(prep.preprocess_ms / 1000.0)
            REQUEST_COUNT.labels(route=canonical.route, status="200").inc()
            REQUEST_LATENCY.labels(route=canonical.route).observe(time.perf_counter() - started)
            return StreamingResponse(_stream_chat(stream), media_type="text/event-stream")

        parsed, prep, model_ms = executor.generate(canonical, model)
        PREPROCESS_LATENCY.labels(route=canonical.route).observe(prep.preprocess_ms / 1000.0)
        MODEL_LATENCY.labels(route=canonical.route, model=canonical.model).observe(model_ms / 1000.0)

        usage = Usage(prompt_tokens=prep.token_estimate, completion_tokens=max(1, len(parsed["content"]) // 4))
        usage.total_tokens = usage.prompt_tokens + usage.completion_tokens
        resp = ChatCompletionResponse(
            model=req.model,
            choices=[
                ChatChoice(
                    message=ChoiceMessage(content=parsed["content"], tool_calls=parsed.get("tool_calls") or None),
                    finish_reason="stop",
                )
            ],
            usage=usage,
        )
        REQUEST_COUNT.labels(route=canonical.route, status="200").inc()
        REQUEST_LATENCY.labels(route=canonical.route).observe(time.perf_counter() - started)
        return resp

    @router.post("/v1/responses", response_model=ResponsesResponse)
    async def responses(req: ResponsesRequest):
        started = time.perf_counter()
        canonical = from_responses_request(req)
        model = registry.get(canonical.model)

        if req.stream:
            stream, prep = executor.stream_generate(canonical, model)
            PREPROCESS_LATENCY.labels(route=canonical.route).observe(prep.preprocess_ms / 1000.0)
            REQUEST_COUNT.labels(route=canonical.route, status="200").inc()
            REQUEST_LATENCY.labels(route=canonical.route).observe(time.perf_counter() - started)
            return StreamingResponse(_stream_responses(stream), media_type="text/event-stream")

        parsed, prep, model_ms = executor.generate(canonical, model)
        PREPROCESS_LATENCY.labels(route=canonical.route).observe(prep.preprocess_ms / 1000.0)
        MODEL_LATENCY.labels(route=canonical.route, model=canonical.model).observe(model_ms / 1000.0)

        usage = Usage(prompt_tokens=prep.token_estimate, completion_tokens=max(1, len(parsed["content"]) // 4))
        usage.total_tokens = usage.prompt_tokens + usage.completion_tokens
        resp = ResponsesResponse(
            model=req.model,
            output=[ResponseOutputText(text=parsed["content"])],
            usage=usage,
        )
        REQUEST_COUNT.labels(route=canonical.route, status="200").inc()
        REQUEST_LATENCY.labels(route=canonical.route).observe(time.perf_counter() - started)
        return resp

    @router.post("/v1/completions")
    async def completions(req: LegacyCompletionRequest) -> dict:
        canonical = from_completion_request(req)
        model = registry.get(canonical.model)
        parsed, prep, _ = executor.generate(canonical, model)
        return {
            "id": f"cmpl-{canonical.request_id}",
            "object": "text_completion",
            "model": req.model,
            "choices": [{"text": parsed["content"], "index": 0, "finish_reason": "stop"}],
            "usage": {
                "prompt_tokens": prep.token_estimate,
                "completion_tokens": max(1, len(parsed["content"]) // 4),
                "total_tokens": prep.token_estimate + max(1, len(parsed["content"]) // 4),
            },
        }

    @router.post("/v1/audio/transcriptions")
    async def transcriptions(
        model: str = Form(...),
        file: UploadFile | None = File(default=None),
        asset_id: str | None = Form(default=None),
        prompt: str | None = Form(default=None),
        language: str | None = Form(default=None),
        response_format: str = Form(default="json"),
    ):
        req = TranscriptionRequest(
            model=model,
            asset_id=asset_id,
            prompt=prompt,
            language=language,
            response_format=response_format,
        )
        model_reg = registry.get(req.model)
        if not model_reg.manifest.supports_transcription:
            raise RunnerError("unsupported_route", "Model does not support transcription.", status_code=400)

        chosen_asset = asset_id
        if file is not None:
            payload = await file.read()
            chosen_asset = ingest.ingest_upload(file.filename or "audio.bin", payload).asset_id
        if not chosen_asset:
            raise RunnerError("asset_ingest_failed", "Provide file or asset_id.", status_code=400)

        asset = ingest.registry.maybe_get(chosen_asset)
        if not asset:
            raise RunnerError("asset_not_found", f"Asset '{chosen_asset}' not found.", status_code=404)

        text = f"[transcription placeholder] asset={asset.asset_id} prompt={req.prompt or ''}".strip()
        if req.response_format == "text":
            return Response(content=text, media_type="text/plain")

        data = {"text": text, "language": req.language or "unknown", "segments": []}
        if req.response_format == "verbose_json":
            data["aether"] = {"asset_id": asset.asset_id, "mime_type": asset.mime_type}
        return data

    @router.post("/v1/audio/translations")
    async def translations(
        model: str = Form(...),
        file: UploadFile | None = File(default=None),
        asset_id: str | None = Form(default=None),
        prompt: str | None = Form(default=None),
        response_format: str = Form(default="json"),
    ):
        req = TranslationRequest(
            model=model,
            asset_id=asset_id,
            prompt=prompt,
            response_format=response_format,
        )
        model_reg = registry.get(req.model)
        if not model_reg.manifest.supports_translation:
            raise RunnerError("unsupported_route", "Model does not support translation.", status_code=400)

        chosen_asset = asset_id
        if file is not None:
            payload = await file.read()
            chosen_asset = ingest.ingest_upload(file.filename or "audio.bin", payload).asset_id
        if not chosen_asset:
            raise RunnerError("asset_ingest_failed", "Provide file or asset_id.", status_code=400)

        asset = ingest.registry.maybe_get(chosen_asset)
        if not asset:
            raise RunnerError("asset_not_found", f"Asset '{chosen_asset}' not found.", status_code=404)

        text = f"[translation placeholder] asset={asset.asset_id} prompt={req.prompt or ''}".strip()
        if req.response_format == "text":
            return Response(content=text, media_type="text/plain")
        return {"text": text, "segments": []}

    @router.post("/v1/audio/speech")
    async def speech(req: SpeechRequest):
        model_reg = registry.get(req.model)
        if not model_reg.manifest.supports_tts:
            raise RunnerError("unsupported_route", "Model/backed route does not support TTS.", status_code=400)
        raise RunnerError("backend_unavailable", "TTS backend adapter not configured yet.", status_code=501)

    return router
