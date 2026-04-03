from __future__ import annotations

from typing import Any

from aether_runner.adapters.generic_hf import GenericHFChatAdapter
from aether_runner.core.config import ModelConfig
from aether_runner.models.schemas import CanonicalRequest, CapabilityManifest


class Gemma4Adapter(GenericHFChatAdapter):
    """Gemma-4 adapter skeleton with modality and family rules.

    This adapter keeps all Gemma-4 specific behavior isolated from generic endpoint code.
    """

    SMALL_AUDIO_HINTS = ("e2b", "e4b")

    def __init__(self, cfg: ModelConfig):
        super().__init__(cfg)

    def _audio_allowed(self) -> bool:
        model_id = self.cfg.id.lower()
        return any(h in model_id for h in self.SMALL_AUDIO_HINTS) or self.cfg.supports.audio

    def capabilities(self) -> CapabilityManifest:
        modalities_in = ["text"]
        if self.cfg.supports.image:
            modalities_in.append("image")
        if self._audio_allowed():
            modalities_in.append("audio")
        if self.cfg.supports.video:
            modalities_in.append("video")

        notes = [
            "audio only guaranteed on E2B/E4B variants",
            "video is treated as frame sequence",
            "thinking tags can be stripped post-parse",
        ]
        return CapabilityManifest(
            id=self.cfg.id,
            backend=self.cfg.backend,
            family="gemma4",
            adapter=self.__class__.__name__,
            modalities_in=modalities_in,
            modalities_out=["text"],
            supports_chat=self.cfg.supports.chat,
            supports_responses=self.cfg.supports.responses,
            supports_function_calling=self.cfg.supports.tools,
            supports_streaming_text=True,
            supports_streaming_audio_out=False,
            supports_transcription=self._audio_allowed(),
            supports_translation=self._audio_allowed(),
            supports_tts=False,
            supports_video_frames=self.cfg.supports.video,
            supports_embeddings=False,
            supports_json_schema=True,
            max_context_tokens=self.cfg.max_context_tokens,
            preferred_routes=["/v1/responses", "/v1/chat/completions", "/v1/audio/transcriptions"],
            notes=notes,
        )

    def normalize_request(self, req: CanonicalRequest) -> CanonicalRequest:
        # Gemma multimodal ordering: media content before trailing text prompt when possible.
        for msg in req.messages:
            if isinstance(msg.content, list):
                msg.content = sorted(
                    msg.content,
                    key=lambda item: 0 if ("image" in item.type or "audio" in item.type or "video" in item.type) else 1,
                )
        return req

    def build_inputs(self, req: CanonicalRequest, assets: list[dict[str, Any]]) -> dict[str, Any]:
        prepared = super().build_inputs(req, assets)
        prepared["gemma_options"] = {
            "enable_thinking": req.execution_hints.enable_thinking,
            "vision_token_budget": req.execution_hints.vision_token_budget,
        }
        return prepared

    def parse_output(self, raw: dict[str, Any]) -> dict[str, Any]:
        text = raw.get("text", "")
        cleaned = text.replace("<think>", "").replace("</think>", "").strip()
        return {"content": cleaned}

    def parse_tools(self, raw: dict[str, Any]) -> list[dict[str, Any]]:
        # Placeholder parser hook for Gemma native function-calling outputs.
        return raw.get("tool_calls", []) if isinstance(raw.get("tool_calls"), list) else []
