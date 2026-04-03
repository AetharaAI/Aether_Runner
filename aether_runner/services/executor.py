from __future__ import annotations

from collections.abc import Iterator
from time import perf_counter

from aether_runner.core.errors import unsupported_modality, unsupported_route
from aether_runner.models.schemas import CanonicalRequest
from aether_runner.services.model_registry import RegisteredModel
from aether_runner.services.preprocess import MultimodalPreprocessor, PreprocessResult


class RunnerExecutor:
    def __init__(self, preprocessor: MultimodalPreprocessor):
        self.preprocessor = preprocessor

    def _assert_route(self, req: CanonicalRequest, model: RegisteredModel) -> None:
        m = model.manifest
        route = req.route
        if route == "/v1/chat/completions" and not m.supports_chat:
            raise unsupported_route(route, req.model)
        if route == "/v1/responses" and not m.supports_responses:
            raise unsupported_route(route, req.model)
        if route == "/v1/audio/transcriptions" and not m.supports_transcription:
            raise unsupported_route(route, req.model)
        if route == "/v1/audio/translations" and not m.supports_translation:
            raise unsupported_route(route, req.model)
        if route == "/v1/audio/speech" and not m.supports_tts:
            raise unsupported_route(route, req.model)

    def _assert_modalities(self, req: CanonicalRequest, model: RegisteredModel) -> None:
        allowed = set(model.manifest.modalities_in)
        for modality in req.modalities():
            if modality not in allowed:
                raise unsupported_modality(modality, req.model)

    def prepare(self, req: CanonicalRequest, model: RegisteredModel) -> tuple[dict, PreprocessResult]:
        self._assert_route(req, model)
        self._assert_modalities(req, model)
        normalized = model.adapter.normalize_request(req)
        prep = self.preprocessor.process(normalized, set(model.manifest.modalities_in))
        prepared = model.adapter.build_inputs(normalized, [a.model_dump() for a in prep.assets])
        return prepared, prep

    def generate(self, req: CanonicalRequest, model: RegisteredModel) -> tuple[dict, PreprocessResult, float]:
        prepared, prep = self.prepare(req, model)
        start = perf_counter()
        raw = model.adapter.generate(prepared)
        model_ms = (perf_counter() - start) * 1000.0
        parsed = model.adapter.parse_output(raw)
        parsed["tool_calls"] = model.adapter.parse_tools(raw)
        return parsed, prep, model_ms

    def stream_generate(self, req: CanonicalRequest, model: RegisteredModel) -> tuple[Iterator[dict], PreprocessResult]:
        prepared, prep = self.prepare(req, model)
        stream = model.adapter.stream_generate(prepared)
        return stream, prep
