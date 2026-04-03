from __future__ import annotations

import time
import uuid
from typing import Any, Literal

from pydantic import BaseModel, Field, model_validator


class CapabilityManifest(BaseModel):
    id: str
    backend: str
    family: str = "generic"
    adapter: str
    modalities_in: list[str] = Field(default_factory=lambda: ["text"])
    modalities_out: list[str] = Field(default_factory=lambda: ["text"])
    supports_chat: bool = True
    supports_responses: bool = True
    supports_function_calling: bool = False
    supports_streaming_text: bool = True
    supports_streaming_audio_out: bool = False
    supports_transcription: bool = False
    supports_translation: bool = False
    supports_tts: bool = False
    supports_video_frames: bool = False
    supports_embeddings: bool = False
    supports_json_schema: bool = False
    max_context_tokens: int = 32768
    preferred_routes: list[str] = Field(default_factory=lambda: ["/v1/chat/completions", "/v1/responses"])
    notes: list[str] = Field(default_factory=list)


class SamplingConfig(BaseModel):
    temperature: float = 1.0
    top_p: float = 0.95
    top_k: int = 64
    max_output_tokens: int = 1024


class ExecutionHints(BaseModel):
    enable_thinking: bool = False
    vision_token_budget: int = 280
    audio_task: str | None = None
    video_fps: int = 1


class ContentItem(BaseModel):
    type: str
    text: str | None = None
    image_url: str | None = None
    audio_url: str | None = None
    input_text: str | None = None
    input_audio: str | None = None
    input_image: str | None = None
    asset_id: str | None = None


class Message(BaseModel):
    role: Literal["system", "user", "assistant", "tool"]
    content: str | list[ContentItem]


class CanonicalRequest(BaseModel):
    request_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    model: str
    route: str
    mode: str = "chat"
    messages: list[Message] = Field(default_factory=list)
    tools: list[dict[str, Any]] = Field(default_factory=list)
    tool_choice: str | dict[str, Any] | None = None
    response_format: dict[str, Any] | None = None
    stream: bool = False
    sampling: SamplingConfig = Field(default_factory=SamplingConfig)
    media: dict[str, list[dict[str, Any]]] = Field(default_factory=lambda: {"audio": [], "images": [], "video": []})
    execution_hints: ExecutionHints = Field(default_factory=ExecutionHints)

    def modalities(self) -> set[str]:
        mods: set[str] = {"text"}
        for msg in self.messages:
            if isinstance(msg.content, list):
                for item in msg.content:
                    t = item.type.lower()
                    if "image" in t:
                        mods.add("image")
                    if "audio" in t:
                        mods.add("audio")
                    if "video" in t:
                        mods.add("video")
        if self.media.get("images"):
            mods.add("image")
        if self.media.get("audio"):
            mods.add("audio")
        if self.media.get("video"):
            mods.add("video")
        return mods


class ChatCompletionRequest(BaseModel):
    model: str
    messages: list[Message]
    stream: bool = False
    temperature: float = 1.0
    top_p: float = 0.95
    max_tokens: int = 1024
    tools: list[dict[str, Any]] = Field(default_factory=list)
    tool_choice: str | dict[str, Any] | None = None
    response_format: dict[str, Any] | None = None


class LegacyCompletionRequest(BaseModel):
    model: str
    prompt: str
    stream: bool = False
    temperature: float = 1.0
    top_p: float = 0.95
    max_tokens: int = 1024


class ResponsesAPIInputItem(BaseModel):
    role: str = "user"
    content: list[ContentItem] = Field(default_factory=list)


class ResponsesRequest(BaseModel):
    model: str
    input: str | list[ResponsesAPIInputItem]
    stream: bool = False
    temperature: float = 1.0
    top_p: float = 0.95
    max_output_tokens: int = 1024
    tools: list[dict[str, Any]] = Field(default_factory=list)
    tool_choice: str | dict[str, Any] | None = None


class TranscriptionRequest(BaseModel):
    model: str
    asset_id: str | None = None
    prompt: str | None = None
    language: str | None = None
    response_format: Literal["json", "verbose_json", "text"] = "json"


class TranslationRequest(BaseModel):
    model: str
    asset_id: str | None = None
    prompt: str | None = None
    response_format: Literal["json", "verbose_json", "text"] = "json"


class SpeechRequest(BaseModel):
    model: str
    input: str
    voice: str = "default"
    format: Literal["wav", "mp3"] = "wav"


class ModelListItem(BaseModel):
    id: str
    object: str = "model"
    created: int = Field(default_factory=lambda: int(time.time()))
    owned_by: str = "aether"
    capabilities: CapabilityManifest


class ModelListResponse(BaseModel):
    object: str = "list"
    data: list[ModelListItem]


class ChoiceMessage(BaseModel):
    role: str = "assistant"
    content: str
    tool_calls: list[dict[str, Any]] | None = None


class ChatChoice(BaseModel):
    index: int = 0
    message: ChoiceMessage
    finish_reason: str = "stop"


class Usage(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


class ChatCompletionResponse(BaseModel):
    id: str = Field(default_factory=lambda: f"chatcmpl-{uuid.uuid4().hex}")
    object: str = "chat.completion"
    created: int = Field(default_factory=lambda: int(time.time()))
    model: str
    choices: list[ChatChoice]
    usage: Usage


class ResponseOutputText(BaseModel):
    type: str = "output_text"
    text: str


class ResponsesResponse(BaseModel):
    id: str = Field(default_factory=lambda: f"resp-{uuid.uuid4().hex}")
    object: str = "response"
    created_at: int = Field(default_factory=lambda: int(time.time()))
    model: str
    output: list[ResponseOutputText]
    usage: Usage


class MediaAsset(BaseModel):
    asset_id: str
    sha256: str
    path: str
    mime_type: str
    size_bytes: int
    modality: Literal["text", "image", "audio", "video", "document", "unknown"] = "unknown"
    metadata: dict[str, Any] = Field(default_factory=dict)


class MediaIngestResponse(BaseModel):
    asset: MediaAsset


class MMParseResponse(BaseModel):
    request_id: str
    model: str
    route: str
    modalities: list[str]
    token_estimate: int
    assets: list[MediaAsset]
    plan: dict[str, Any]


class VideoUnderstandRequest(BaseModel):
    model: str
    asset_id: str | None = None
    fps: int = 1
    frame_budget: int = 32
    prompt: str = "Summarize this video and list notable events."


class VideoUnderstandResponse(BaseModel):
    model: str
    summary: str
    scene_events: list[dict[str, Any]] = Field(default_factory=list)


class AetherError(BaseModel):
    error: dict[str, Any]


class HealthResponse(BaseModel):
    status: Literal["ok", "not_ready"]
    detail: dict[str, Any] = Field(default_factory=dict)


class ModelsConfigValidation(BaseModel):
    models: list[CapabilityManifest]

    @model_validator(mode="after")
    def check_unique_ids(self) -> "ModelsConfigValidation":
        ids = [m.id for m in self.models]
        if len(ids) != len(set(ids)):
            raise ValueError("Duplicate model ids found.")
        return self
