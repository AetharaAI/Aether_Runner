from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from aether_runner.adapters.base import ModelAdapter
from aether_runner.backends.transformers_backend import TransformersBackend
from aether_runner.core.config import ModelConfig
from aether_runner.models.schemas import CanonicalRequest, CapabilityManifest


class GenericHFChatAdapter(ModelAdapter):
    def __init__(self, cfg: ModelConfig):
        self.cfg = cfg
        self.backend = TransformersBackend(
            model_path=cfg.path,
            dtype=cfg.dtype,
            device_map=cfg.device_map,
            trust_remote_code=cfg.trust_remote_code,
        )

    def maybe_load(self, eager: bool = False) -> None:
        if eager:
            self.backend.load()

    def capabilities(self) -> CapabilityManifest:
        return CapabilityManifest(
            id=self.cfg.id,
            backend=self.cfg.backend,
            family="generic_hf",
            adapter=self.__class__.__name__,
            modalities_in=[m for m, on in self.cfg.supports.model_dump().items() if on and m in {"text", "image", "audio", "video"}],
            modalities_out=["text"],
            supports_chat=self.cfg.supports.chat,
            supports_responses=self.cfg.supports.responses,
            supports_function_calling=self.cfg.supports.tools,
            supports_streaming_text=True,
            supports_streaming_audio_out=False,
            supports_transcription=self.cfg.supports.transcription,
            supports_translation=self.cfg.supports.translation,
            supports_tts=self.cfg.supports.tts,
            supports_video_frames=self.cfg.supports.video,
            supports_embeddings=self.cfg.supports.embeddings,
            supports_json_schema=True,
            max_context_tokens=self.cfg.max_context_tokens,
        )

    def normalize_request(self, req: CanonicalRequest) -> CanonicalRequest:
        return req

    def build_inputs(self, req: CanonicalRequest, assets: list[dict[str, Any]]) -> dict[str, Any]:
        lines: list[str] = []
        for msg in req.messages:
            if isinstance(msg.content, str):
                lines.append(f"{msg.role}: {msg.content}")
            else:
                chunks = []
                for item in msg.content:
                    if item.text:
                        chunks.append(item.text)
                    elif item.asset_id:
                        chunks.append(f"[{item.type}:{item.asset_id}]")
                lines.append(f"{msg.role}: {' '.join(chunks)}")
        prompt = "\n".join(lines) + "\nassistant:"
        return {
            "prompt": prompt,
            "sampling": req.sampling.model_dump(),
            "assets": assets,
            "request": req,
        }

    def generate(self, prepared: dict[str, Any]) -> dict[str, Any]:
        prompt = prepared["prompt"]
        sample = prepared["sampling"]
        try:
            text = self.backend.generate_text(
                prompt,
                max_new_tokens=sample.get("max_output_tokens", 256),
                temperature=sample.get("temperature", 1.0),
                top_p=sample.get("top_p", 0.95),
            )
        except Exception:
            # Keep runner usable even when model weights are absent.
            text = "[aether-runner] model backend unavailable; run on GPU host with model weights mounted."
        return {"text": text}

    def stream_generate(self, prepared: dict[str, Any]) -> Iterator[dict[str, Any]]:
        text = self.generate(prepared)["text"]
        for token in text.split():
            yield {"delta": token + " "}

    def parse_output(self, raw: dict[str, Any]) -> dict[str, Any]:
        return {"content": raw.get("text", "")}

    def parse_tools(self, raw: dict[str, Any]) -> list[dict[str, Any]]:
        return []
