# RFC: Aether Runner

## Multimodal Native Fallback Inference Plane

**Status:** Draft v1
**Owner:** AetherPro
**Purpose:** Build a Transformers-native, multimodal, OpenAI-compatible model runner for models that do not run cleanly in vLLM, especially newly released multimodal and any-to-any models.

## 1. Problem Statement

vLLM is the primary inference plane for stable, supported models. It works well until it does not.

Recent failures exposed a recurring gap:

* some new multimodal models fall back to incomplete backend paths,
* some models require capabilities beyond what vLLM exposes cleanly,
* some models support audio, image, video, or any-to-any flows that are either unsupported or partially surfaced,
* model-family support often lags behind model release.

This causes repeated engineering waste:

* model works in native Transformers but not in vLLM,
* model loads but does not expose all modalities,
* model supports multimodal reasoning but runtime path strips or degrades capabilities,
* new family support becomes a waiting game.

Aether Runner fixes that by creating a second inference lane.

## 2. Goals

Aether Runner must:

1. Expose an **OpenAI-compatible API surface** so the existing gateway can route to it without special handling.
2. Include a **mandatory multimodal preprocessor path** for text, image, audio, video, and document-like inputs.
3. Support **model-family adapters** so model quirks are isolated and reusable.
4. Preserve **full model capability** where possible, especially:

   * text generation
   * image understanding
   * audio transcription / translation
   * video-as-frames understanding
   * function calling
   * any-to-any routing where supported
5. Serve as the **fallback inference plane** when vLLM support is missing, partial, or broken.
6. Be deployable as **one model per container** with predictable resource isolation.
7. Provide enough observability to diagnose:

   * model load failures
   * preprocessing failures
   * backend incompatibilities
   * capability mismatches

## 3. Non-Goals

Aether Runner is not:

* a replacement for vLLM on supported models,
* a training platform,
* a workflow engine,
* a generic orchestrator,
* a hacky one-off wrapper for a single model.

It is a **fallback-native model serving layer**.

## 4. Strategic Thesis

**Standardize the surface, not the engine.**

The gateway should see the same interface whether the backend is:

* vLLM
* Transformers
* family-specific model logic
* ASR engine
* TTS engine
* future realtime audio stack

The gateway should not care how the model is run. It should only care that:

* the route exists,
* the model is available,
* the response shape is correct,
* the capability manifest is truthful.

## 5. Primary Use Cases

### 5.1 Immediate

* Run Gemma-family multimodal models when vLLM support is incomplete.
* Run Phi-family or other fresh models that work in Transformers before they work in vLLM.
* Preserve multimodal capability without losing audio/image/video support.

### 5.2 Ongoing

* Intake lane for new open models.
* Research lane for multimodal and any-to-any models.
* Capability-preserving lane for models whose runtimes expose more than vLLM currently surfaces.
* Internal infrastructure primitive for Perceptor-class and media-heavy workloads.

## 6. Functional Requirements

## 6.1 API Compatibility

Must expose these routes:

### Core OpenAI-compatible routes

* `GET /v1/models`
* `POST /v1/chat/completions`
* `POST /v1/completions`
* `POST /v1/responses`

### Audio routes

* `POST /v1/audio/transcriptions`
* `POST /v1/audio/translations`
* `POST /v1/audio/speech`

### Optional / model-specific routes

* `POST /v1/embeddings`

### Aether-native routes

* `GET /aether/v1/capabilities`
* `POST /aether/v1/media/ingest`
* `POST /aether/v1/mm/parse`
* `POST /aether/v1/video/understand`
* `GET /healthz`
* `GET /readyz`
* `GET /livez`
* `GET /metrics`

## 6.2 Mandatory Multimodal Support

The preprocessor is **not optional**.

If the model supports a modality, the runner must be capable of preparing and feeding that modality correctly.

Supported input categories:

* text
* image
* audio
* video
* PDF/document-as-images
* asset references
* multipart uploads
* local file paths
* URLs if explicitly allowed

## 6.3 Capability Truthfulness

Each model must register a capability manifest that defines:

* modalities in
* modalities out
* tool calling support
* structured output support
* streaming support
* audio support
* video support
* max context
* preferred routes
* adapter name
* backend type

No fake support. No silent downgrade.

## 7. Architecture

## 7.1 High-Level Components

### 1. API Layer

FastAPI service exposing compatible routes.

### 2. Request Normalizer

Converts all incoming requests into a canonical internal request format.

### 3. Multimodal Preprocessor

Mandatory preprocessing stage that:

* ingests media,
* normalizes formats,
* extracts metadata,
* creates modality execution plan,
* packages processor/model inputs.

### 4. Capability Router

Chooses the correct adapter and backend based on:

* model ID
* requested route
* modality set
* capability manifest

### 5. Model Adapter

Encapsulates family-specific logic:

* processor loading
* prompt construction
* chat template handling
* thinking mode control
* tool parsing
* modality ordering
* response parsing

### 6. Execution Backend

Executes inference using:

* Transformers
* family-specific implementation
* ASR backend
* TTS backend

### 7. Postprocessor

Converts raw backend output into OpenAI-compatible response shapes.

### 8. Media Cache / Asset Store

Stores:

* uploaded assets
* normalized media
* extracted frames
* derived intermediate artifacts
* metadata

### 9. Telemetry Layer

Captures:

* preprocess latency
* model latency
* token counts
* frame counts
* audio seconds
* memory usage
* route-level errors

## 7.2 Deployment Topology

Recommended:

* one model per container
* one runner instance per model
* gateway routes to runner instance
* shared utility stack for ffmpeg / OCR / VAD if needed

Why:

* clean resource accounting
* simpler restart behavior
* easier debugging
* cleaner model isolation

## 8. Canonical Internal Request Schema

Every route must normalize into one internal IR.

```json
{
  "request_id": "uuid",
  "model": "gemma-4-e4b-it",
  "mode": "chat",
  "route": "/v1/chat/completions",
  "messages": [
    {
      "role": "system",
      "content": [
        {"type": "text", "text": "You are a helpful assistant."}
      ]
    },
    {
      "role": "user",
      "content": [
        {"type": "input_audio", "asset_id": "aud_001"},
        {"type": "input_image", "asset_id": "img_001"},
        {"type": "text", "text": "Describe this and transcribe the audio."}
      ]
    }
  ],
  "tools": [],
  "response_format": null,
  "stream": true,
  "sampling": {
    "temperature": 1.0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 1024
  },
  "execution_hints": {
    "enable_thinking": false,
    "vision_token_budget": 280,
    "audio_task": "transcribe",
    "video_fps": 1
  }
}
```

## 9. Capability Manifest Schema

```json
{
  "id": "gemma-4-e4b-it",
  "backend": "transformers",
  "adapter": "Gemma4Adapter",
  "modalities_in": ["text", "image", "audio"],
  "modalities_out": ["text"],
  "supports_chat": true,
  "supports_responses": true,
  "supports_function_calling": true,
  "supports_transcription": true,
  "supports_translation": true,
  "supports_tts": false,
  "supports_video_frames": true,
  "supports_streaming_text": true,
  "supports_streaming_audio_out": false,
  "max_context_tokens": 131072
}
```

## 10. Multimodal Preprocessor Specification

## 10.1 Responsibilities

The preprocessor must:

* validate input modality and media type,
* ingest and persist media assets,
* compute hashes for dedupe,
* normalize formats,
* derive metadata,
* create model-specific modality plan,
* package processor-ready inputs.

## 10.2 Subsystems

### Audio

* decoder
* resampler
* mono conversion
* segmenter
* optional VAD
* optional diarization
* task framing for ASR / translation

### Image

* normalization
* orientation fix
* RGB conversion
* safe resize policy
* token budget planning
* OCR hint routing

### Video

* demux
* frame extraction
* configurable fps
* optional audio separation
* optional OCR / ASR side-path
* frame packaging

### Document/PDF

* rasterization per page
* OCR path
* page-to-image treatment

## 10.3 Preprocessor Stages

### Stage A: Ingest

* save asset
* compute hash
* detect mime
* verify size
* assign asset ID

### Stage B: Normalize

* convert to standard forms per modality

### Stage C: Enrich

* extract metadata
* estimate token cost
* detect modality-specific constraints

### Stage D: Plan

* decide what input representation to feed the model

Examples:

* audio direct
* image direct
* video as frames
* document as page images
* OCR-first then prompt
* ASR-first then reasoning
* mixed multimodal ordering

### Stage E: Package

* use adapter + processor to build final model inputs

## 11. Adapter Layer

## 11.1 Adapter Contract

Each adapter must implement:

```python
class ModelAdapter(Protocol):
    def capabilities(self) -> CapabilityManifest: ...
    def load(self, cfg): ...
    def build_inputs(self, req, assets): ...
    def generate(self, prepared): ...
    def stream_generate(self, prepared): ...
    def parse_output(self, raw): ...
    def parse_tools(self, raw): ...
```

## 11.2 First Adapters

* `Gemma4Adapter`
* `PhiAdapter`
* `GenericHFAdapter`
* `WhisperLikeASRAdapter`
* `TTSAdapterBase`

## 11.3 Gemma4 Adapter Requirements

The Gemma adapter must handle:

* `AutoProcessor`
* multimodal ordering
* optional reasoning control
* thinking tag handling
* audio support gating for small variants
* video via frame sequence
* function calling parsing

Gemma 4’s model card explicitly describes:

* four sizes: E2B, E4B, 26B A4B, 31B,
* audio support on the small models only,
* image support across the family,
* video via frames,
* multimodal interleaving,
* function calling support.  

## 12. Endpoint Behavior

## 12.1 `GET /v1/models`

Returns registered models in OpenAI-compatible shape plus Aether extension metadata:

* capabilities
* modalities
* backend
* adapter
* max context

## 12.2 `POST /v1/chat/completions`

Supports:

* text-only
* text + image
* text + audio
* text + image + audio
* text + video via frame extraction
* tools
* streaming text output

## 12.3 `POST /v1/responses`

Preferred modern route.
Used for:

* multimodal input arrays
* tool use
* future expansion without legacy chat baggage

## 12.4 `POST /v1/completions`

Legacy compatibility only.

## 12.5 `POST /v1/audio/transcriptions`

Accepts:

* multipart audio
* asset ID
* local file ref
* URL if allowed

Returns:

* transcript
* optionally segments
* optional Aether extension metadata

## 12.6 `POST /v1/audio/translations`

Like transcription, but framed as translation.

## 12.7 `POST /v1/audio/speech`

Routes to TTS-capable backend only.
This route is backend-pluggable, not tied to Gemma.

## 12.8 `POST /aether/v1/video/understand`

Purpose:

* video ingestion and understanding
* optional frame summaries
* scene event extraction
* OCR / ASR side paths
* structured output

## 12.9 `POST /aether/v1/mm/parse`

Debug / preprocessing route that returns:

* extracted metadata
* OCR text
* ASR text
* frame counts
* chosen execution plan

## 13. Execution Backends

## 13.1 Backend Types

* `transformers`
* `family_custom`
* `asr_native`
* `tts_native`
* `realtime_native`

## 13.2 Transformers Backend

Default fallback lane.

Load pattern:

* processor from pretrained
* model from pretrained or family-specific class
* device map auto or configured
* dtype auto or configured
* generation via adapter

## 13.3 Why this exists

Because some models work in native Transformers before they work in vLLM. That is the whole point.

## 14. Streaming

## 14.1 Required in v1

* SSE text streaming for chat/responses

## 14.2 Desired next

* streaming ASR deltas
* chunked TTS output
* unified realtime websocket path

## 15. Tool Calling

Must support:

* tool schema input
* tool choice
* canonical function-call output
* adapter-based parser

No fake tool support.

## 16. Security Requirements

Must include:

* bearer auth on all routes
* request size limits
* media type allowlist
* SSRF-safe URL fetch path
* temp file cleanup
* structured audit logs

## 17. Observability

## 17.1 Metrics

Per request:

* preprocess_ms
* model_ms
* total_ms
* input_tokens
* output_tokens
* frame_count
* audio_seconds
* gpu_mem_peak
* cache_hit

## 17.2 Logs

Structured JSON logs:

* request_id
* model
* adapter
* backend
* route
* modalities
* timings
* error_stage
* exception_class

## 18. Failure Model

Return explicit typed errors:

* `unsupported_modality`
* `unsupported_route`
* `asset_ingest_failed`
* `audio_decode_failed`
* `video_decode_failed`
* `processor_failed`
* `adapter_failed`
* `model_load_failed`
* `backend_unavailable`
* `tool_schema_invalid`

No silent fallback without disclosure.

## 19. Config Model

## 19.1 Runner Config

```yaml
runner:
  host: 0.0.0.0
  port: 8010
  auth_mode: bearer
  temp_dir: /tmp/aether-runner
  media_cache_dir: /cache/media
  asset_ttl_seconds: 86400
  enable_realtime: false
```

## 19.2 Model Config

```yaml
model:
  id: gemma-4-e4b-it
  path: /models/google/gemma-4-E4B-it
  adapter: gemma4
  backend: transformers
  dtype: auto
  device_map: auto
  trust_remote_code: false
  supports:
    text: true
    image: true
    audio: true
    video: true
    tools: true
  defaults:
    temperature: 1.0
    top_p: 0.95
    top_k: 64
    max_output_tokens: 1024
    enable_thinking: false
    vision_token_budget: 280
```

## 20. Milestones

## Phase 0

Scaffold and schemas

* FastAPI app
* auth middleware
* model registry
* `/healthz`, `/readyz`, `/v1/models`

## Phase 1

Text + image + responses

* canonical IR
* media ingest
* image preprocessing
* `Gemma4Adapter`
* `/v1/chat/completions`
* `/v1/responses`
* SSE streaming

## Phase 1.5

Audio in

* audio decode
* transcription / translation
* E2B/E4B support
* `/v1/audio/transcriptions`
* `/v1/audio/translations`

## Phase 2

Video and speech

* frame extraction
* `/aether/v1/video/understand`
* `/v1/audio/speech`
* TTS backend abstraction

## Phase 3

Realtime

* WS path
* streaming ASR
* streaming TTS
* duplex loop

## 21. Acceptance Criteria

v1 is complete when:

1. A Gemma 4 small model can be loaded through Transformers backend.
2. Gateway can hit `/v1/models` and `/v1/chat/completions` unchanged.
3. Image input works through the multimodal preprocessor.
4. Audio transcription route works for supported models/backends.
5. Capability manifest returns correct modality info.
6. Streaming text works.
7. Errors are explicit and typed.
8. Logs and metrics are usable for debugging.

## 22. First Codex Task

Give Codex this exact first build objective:

**Build Aether Runner v1 scaffold with:**

* FastAPI app
* bearer auth middleware
* health endpoints
* model registry
* capability manifest schema
* canonical request schema
* media ingest service
* image/audio/video preprocessing skeletons
* `ModelAdapter` interface
* `Gemma4Adapter` skeleton
* `/v1/models`
* `/v1/chat/completions`
* `/v1/responses`
* `/v1/audio/transcriptions`
* `/v1/audio/translations`
* stub `/v1/audio/speech`
* SSE streaming support
* structured JSON logs
* unit tests for normalization and capability validation

## 23. Final Decision

Build it.

This is no longer “special handling for one weird model.”
This is an infrastructure gap that has now repeated enough times to justify a dedicated fallback inference plane.


