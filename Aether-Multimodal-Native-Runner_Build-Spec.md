## RFC: Aether Multimodal Native Runner

Not a toy wrapper. A real **multimodal fallback inference plane** that sits beside vLLM and exposes the same contract to your gateway, while handling models that are too new, too weird, or too multimodal for vLLM to support cleanly yet. That is justified by the pain you just hit: vLLM’s OpenAI-compatible server is strong, but model support is uneven by family; today it supports OpenAI-shaped endpoints like chat/completions, completions, responses, embeddings, transcriptions, and translations, with multimodal chat input support, while also warning that some models fall back to a Transformers backend. OpenAI’s current API surface also splits cleanly across REST and Realtime, with Responses recommended for new work, REST audio routes for transcription/translation/speech, and Realtime for low-latency multimodal audio interactions. ([vLLM][1])

For Gemma 4 specifically, your fallback runner is not optional if you want first-class multimodal behavior. The Gemma 4 small models, E2B and E4B, support text, image, and audio; the larger 26B A4B and 31B support text and image; the family also supports video understanding through frame processing, multimodal interleaving, function calling, and variable image token budgets.   

# RFC: Aether Multimodal Native Runner

## Working name

**Aether Runner**
Internal role: **Transformers-native multimodal inference plane with OpenAI-compatible surface**

## 1. Purpose

Build a runner that:

* serves text, image, audio, and video-capable models natively through Transformers or model-specific backends,
* preserves your existing gateway contract,
* exposes OpenAI-compatible endpoints first,
* adds Aether extensions where OpenAI/vLLM shapes are insufficient,
* centralizes multimodal preprocessing so model capability is available without writing one-off glue per model.

## 2. Core thesis

**Standardize the surface, not the engine.**

Your gateway should route to:

* vLLM backends when supported,
* Aether Runner when vLLM support is partial, broken, or missing,
* specialized inference workers for ASR, TTS, VLM, any-to-any, or video models.

The gateway should not need to know whether the target backend is:

* vLLM,
* Transformers,
* TGI,
* or a model-family-specific worker.

## 3. Design principles

1. **Gateway contract stability**
   Every backend must look OpenAI-compatible to the router.

2. **Multimodal preprocessing is first-class**
   Not optional. Every request goes through a media normalization and modality planning stage.

3. **Model adapters own quirks**
   Chat templates, processor classes, thinking tags, tokenizer behavior, vision budgets, audio prompts, and response parsing live in adapters, not generic endpoint code.

4. **Media in, canonical IR out**
   Every endpoint converts request payloads into one internal multimodal request format before execution.

5. **Backend pluggability**
   One API surface, multiple execution engines.

6. **Capability discovery**
   The server must advertise what each model can actually do.

7. **Fail closed**
   If a model cannot handle a modality or route, return explicit capability errors, not silent degradation.

## 4. Non-goals

* Replacing vLLM for supported mature models.
* Building a training platform.
* Building a generic workflow engine.
* Hiding model incompatibilities behind fake success.
* Supporting every multimodal model family in v1.

## 5. Product outcome

Aether Runner becomes:

* your **new-model intake lane**,
* your **multimodal experimentation lane**,
* your **compatibility lane**,
* your **research lane**,
* and eventually the **reference fallback plane** for the whole Aether stack.

# 6. External compatibility target

## 6.1 Must match

Implement an OpenAI-compatible REST surface that covers the routes your gateway and clients are most likely to use:

* `GET /v1/models`
* `POST /v1/chat/completions`
* `POST /v1/completions`
* `POST /v1/responses`
* `POST /v1/embeddings`
* `POST /v1/audio/transcriptions`
* `POST /v1/audio/translations`
* `POST /v1/audio/speech`

That aligns with the union of the current vLLM OpenAI-compatible server and the current OpenAI REST surface for text, vision, embeddings, speech-to-text, and text-to-speech. ([vLLM][1])

## 6.2 Should match

Phase 2:

* `POST /v1/realtime/sessions`
* `WS /v1/realtime`
* optional WebRTC offer/answer helper routes

OpenAI’s Realtime API is the right shape to mirror for low-latency multimodal audio and speech-to-speech style interaction. ([OpenAI Developers][2])

## 6.3 Aether extensions

Because neither OpenAI nor vLLM gives you a perfect “any-to-any everything” surface, add explicit Aether routes:

* `POST /aether/v1/media/ingest`
* `POST /aether/v1/video/understand`
* `POST /aether/v1/mm/parse`
* `POST /aether/v1/mm/plan`
* `POST /aether/v1/audio/diarize`
* `POST /aether/v1/audio/vad`
* `POST /aether/v1/audio/segment`
* `POST /aether/v1/vision/ocr`
* `POST /aether/v1/vision/detect`
* `POST /aether/v1/vision/ground`
* `POST /aether/v1/tool/schema/validate`

These are not gateway-default routes. They are native power routes for internal use and advanced clients.

# 7. Capability model

Every loaded model gets a runtime capability manifest.

## 7.1 Capability manifest schema

```json
{
  "id": "gemma-4-e4b-it",
  "backend": "transformers",
  "family": "gemma4",
  "modalities_in": ["text", "image", "audio"],
  "modalities_out": ["text"],
  "supports_chat": true,
  "supports_responses": true,
  "supports_function_calling": true,
  "supports_streaming_text": true,
  "supports_streaming_audio_out": false,
  "supports_audio_transcription": true,
  "supports_audio_translation": true,
  "supports_tts": false,
  "supports_video_frames": true,
  "supports_embeddings": false,
  "supports_json_schema": true,
  "max_context_tokens": 131072,
  "preferred_routes": [
    "/v1/responses",
    "/v1/chat/completions",
    "/v1/audio/transcriptions"
  ],
  "adapter": "Gemma4Adapter",
  "processor": "AutoProcessor",
  "notes": [
    "audio only on E2B/E4B",
    "video handled as frame sequence",
    "thinking tags need post-parse"
  ]
}
```

## 7.2 Why this matters

Your gateway can ask the runner:

* what this model supports,
* what routes should be enabled,
* what modality combinations are legal,
* whether it should be used for ASR, TTS, VLM, OCR, tool use, or simple chat.

# 8. Core architecture

## 8.1 Components

1. **API Layer**
   FastAPI app exposing OpenAI-compatible and Aether-native routes.

2. **Request Normalizer**
   Converts incoming OpenAI/Aether payloads into canonical internal request objects.

3. **Multimodal Preprocessor**
   Mandatory stage.
   Handles media ingest, decode, normalization, segmentation, frame extraction, resampling, token budgeting, and processor packaging.

4. **Capability Router**
   Selects adapter + execution backend based on model manifest and request modalities.

5. **Model Adapter**
   Family-specific logic:

   * chat template construction
   * processor invocation
   * generation config rules
   * thinking enable/disable
   * structured output parsing
   * tool call parsing
   * modality ordering

6. **Execution Backend**
   One of:

   * Transformers local
   * model-family custom runner
   * TTS engine wrapper
   * ASR engine wrapper
   * future Realtime engine

7. **Postprocessor**
   Converts raw outputs into OpenAI-compatible response shapes.

8. **Media Cache**
   Deduplicates repeated image/audio/video inputs by hash.

9. **Artifact Store**
   Temporary or persistent storage for uploaded/normalized media.

10. **Telemetry Layer**
    Logs latency, preprocessing time, model time, tokens, frames, seconds of audio, VRAM, cache hit rate.

## 8.2 Process layout

Recommended:

* one container per loaded model,
* one control-plane API per host,
* one worker process per model instance,
* optional sidecars for ffmpeg, OCR, VAD, diarization.

For early v1, simplest is:

* single-process FastAPI control plane,
* model workers launched as subprocesses or separate containers,
* gateway points to a runner registry.

# 9. Canonical internal request format

Everything maps to this.

```json
{
  "request_id": "uuid",
  "model": "gemma-4-e4b-it",
  "route": "/v1/chat/completions",
  "mode": "chat",
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
        {"type": "input_audio", "asset_id": "aud_123"},
        {"type": "input_image", "asset_id": "img_456"},
        {"type": "text", "text": "Summarize this and extract tasks."}
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
  "media": {
    "audio": [{"asset_id": "aud_123", "seconds": 23.2, "sample_rate": 16000}],
    "images": [{"asset_id": "img_456", "width": 1920, "height": 1080}],
    "video": []
  },
  "execution_hints": {
    "enable_thinking": false,
    "vision_token_budget": 280,
    "audio_task": "transcribe",
    "video_fps": 1
  }
}
```

# 10. Multimodal preprocessor path

This is the heart of the thing.

## 10.1 Input types

Support all of:

* raw bytes
* multipart file upload
* local file path
* remote URL
* file IDs
* prior asset IDs
* base64 payloads

## 10.2 Preprocessor pipeline

### Stage A: ingest

* validate media type
* persist temp asset
* compute SHA256
* dedupe by hash
* detect mime
* detect codecs

### Stage B: normalize

* audio → PCM16 / float32 / target sample rate
* image → RGB tensor / standard orientation / safe size
* video → demux, frame extraction, optional audio split
* document/PDF → per-page rasterization if needed

### Stage C: enrich

* audio: duration, channels, language guess, VAD segments
* image: dimensions, aspect ratio, OCR hint score
* video: fps, duration, frame count, keyframe plan
* all: token budget estimate

### Stage D: modality plan

Decide what the model sees:

* direct raw modality
* frames + text prompt
* audio chunks + task prompt
* OCR-first then vision
* ASR-first then LLM
* dual path
* fail if model manifest says unsupported

### Stage E: processor packaging

Use model adapter to build:

* processor inputs
* chat template
* ordered multimodal prompt
* generation-ready tensors

## 10.3 Required submodules

* `AudioDecoder`
* `AudioResampler`
* `VADSegmenter`
* `Diarizer` optional
* `ImageNormalizer`
* `VideoFrameExtractor`
* `VideoSampler`
* `PdfRasterizer`
* `OCRBridge`
* `MediaCache`
* `AssetRegistry`

## 10.4 Modality ordering rules

Model-specific.
For Gemma 4, you should codify what the model card says:

* image/audio before text where appropriate,
* configurable visual token budget,
* E2B/E4B audio support only,
* video treated as frame sequences. 

# 11. Endpoint specification

## 11.1 `GET /v1/models`

Returns models available on this runner.

Add Aether metadata under each model:

* `capabilities`
* `modalities_in`
* `modalities_out`
* `max_context_tokens`
* `backend`
* `adapter`

## 11.2 `POST /v1/chat/completions`

Purpose:

* OpenAI-compatible chat
* supports multimodal user content
* supports tools
* supports streaming

Behavior:

* normalize message content into canonical IR
* run preprocessor
* adapter builds model-native prompt
* execute
* postprocess into `choices[0].message`

Must support:

* text-only
* text + image
* text + audio
* text + image + audio
* optional video via extracted frames

## 11.3 `POST /v1/responses`

Make this the preferred modern route.
Why:

* cleaner future-proof envelope
* easier for multi-item inputs
* easier tool orchestration
* closer to where the ecosystem is going. OpenAI recommends Responses for new projects, while vLLM already exposes a compatible Responses API. ([OpenAI Developers][3])

## 11.4 `POST /v1/completions`

Legacy support only.
Text-only unless a model adapter explicitly allows multimodal prompt flattening.

## 11.5 `POST /v1/embeddings`

Optional in v1.
Implement only for models that are actually embedding-capable.
Do not fake embeddings from generation models unless you explicitly expose that as a separate approximate mode.

## 11.6 `POST /v1/audio/transcriptions`

Multipart upload or asset reference.
Return OpenAI-shaped transcription object.
Support:

* plain transcript
* verbose segments
* optional diarization extension

## 11.7 `POST /v1/audio/translations`

Same as transcription, but target output normalization.
OpenAI and vLLM both model speech-to-text as transcriptions plus translations. ([OpenAI Developers][4])

## 11.8 `POST /v1/audio/speech`

For TTS-capable backends only.
This route should not assume every LLM can emit speech.
Instead route to:

* Voxtral TTS
* Chatterbox
* Kokoro
* OmniVoice-like engines
* future speech heads

Return:

* audio bytes
* or event stream if streaming supported

## 11.9 `POST /aether/v1/video/understand`

Input:

* uploaded file
* URL
* asset ID

Processing:

* frame extraction
* optional audio split
* configurable fps / frame budget
* optional OCR + ASR sidecar path
* pass frames and derived text/audio into adapter

Output:

* summary
* scene events
* timestamps
* optional structured timeline

## 11.10 `POST /aether/v1/mm/parse`

Purpose:

* return canonical parsed media understanding without generation
* good for preprocessing debug and pipeline inspection

Output:

* OCR text
* ASR text
* frame captions
* hashes
* token estimates
* selected execution plan

## 11.11 Realtime

Phase 2.
Mirror WebSocket session semantics for:

* input audio stream
* partial ASR deltas
* partial text deltas
* optional response audio

OpenAI’s Realtime API is the right conceptual template here. ([OpenAI Developers][2])

# 12. Adapter system

## 12.1 Adapter interface

```python
class ModelAdapter(Protocol):
    def capabilities(self) -> CapabilityManifest: ...
    def normalize_request(self, req: CanonicalRequest) -> CanonicalRequest: ...
    def build_inputs(self, req: CanonicalRequest) -> PreparedInputs: ...
    def generate(self, prepared: PreparedInputs) -> RawModelOutput: ...
    def stream_generate(self, prepared: PreparedInputs) -> Iterator[Delta]: ...
    def parse_output(self, raw: RawModelOutput) -> CanonicalOutput: ...
    def parse_tools(self, raw: RawModelOutput) -> list[ToolCall]: ...
```

## 12.2 First adapters

* `Gemma4Adapter`
* `PhiAdapter`
* `GenericHFChatAdapter`
* `WhisperLikeASRAdapter`
* `TTSAdapterBase`
* `AnyToAnyAdapterBase`

## 12.3 Gemma 4 adapter responsibilities

* `AutoProcessor` handling
* multimodal order enforcement
* thinking token control
* response parsing
* audio gate for E2B/E4B only
* image/video frame packaging
* function-calling parse rules

That behavior should follow the model card, not generic guesswork. 

# 13. Execution backends

## 13.1 Backend enum

* `transformers`
* `custom_family`
* `asr_native`
* `tts_native`
* `realtime_native`

## 13.2 Transformers backend

Use when:

* model loads with HF classes,
* processor exists,
* vLLM support is absent or broken,
* multimodal preprocessing must be preserved.

Preferred load pattern for initial v1:

* `AutoProcessor.from_pretrained`
* `AutoModelForCausalLM.from_pretrained` or family-specific class
* `device_map=auto`
* configurable `dtype`
* optional quantization config
* generation through adapter

## 13.3 Why not one giant generic backend

Because models lie.
Or rather: model cards simplify, configs differ, and processors drift.
Family adapters keep the blast radius contained.

# 14. Streaming

## 14.1 Text streaming

Required in v1:

* SSE stream for chat/responses
* delta chunks
* final usage block

## 14.2 Audio streaming

Phase 1.5 or 2:

* chunked audio events from TTS engines
* chunked ASR deltas where backend supports it
* optional duplex mode later

## 14.3 Video streaming

Not required.
Treat video as uploaded or referenced asset, then stream partial analysis deltas if useful.

# 15. Tool calling

## 15.1 Required

* accept `tools`
* accept `tool_choice`
* support function-call-style outputs
* parse model-native tool responses into canonical OpenAI-style function calls

## 15.2 Why

Gemma 4 advertises native function-calling support, and your harness model strategy depends on tools as a first-class primitive. 

# 16. Config model

## 16.1 Runner config

```yaml
runner:
  host: 0.0.0.0
  port: 8010
  auth_mode: bearer
  temp_dir: /tmp/aether-runner
  media_cache_dir: /cache/media
  asset_ttl_seconds: 86400
  max_upload_mb:
    image: 50
    audio: 200
    video: 1000
  enable_realtime: false
```

## 16.2 Model config

```yaml
model:
  id: gemma-4-e4b-it
  path: /models/google/gemma-4-E4B-it
  adapter: gemma4
  backend: transformers
  dtype: auto
  device_map: auto
  trust_remote_code: false
  max_context_tokens: 131072
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

# 17. Security

## 17.1 Required

* bearer auth for all routes, not just `/v1`
* per-route auth middleware
* deny unauthenticated `/docs`, `/metrics`, `/aether/*`
* request body size limits
* media type allowlist
* URL fetch allowlist or SSRF-safe fetcher
* temp-file cleanup
* structured audit logs

This matters because vLLM’s own docs warn that `--api-key` covers only `/v1` routes and is not sufficient to secure the whole server. Do not copy that limitation into your runner. ([vLLM][5])

## 17.2 Optional later

* signed asset URLs
* per-model ACLs
* org/project scoped tokens
* request signing between gateway and runner

# 18. Observability

## 18.1 Metrics

Per request:

* total latency
* preprocess latency
* model latency
* tokens in/out
* frames extracted
* audio seconds
* OCR chars
* cache hit/miss
* GPU memory peak
* CPU RAM peak

## 18.2 Logs

Structured JSON:

* request_id
* model_id
* adapter
* route
* modalities_in
* status
* failure_stage
* exception_class
* timings

## 18.3 Debug artifacts

Optional debug save:

* normalized prompt
* extracted frames thumbnails
* OCR text
* ASR transcript
* final processor inputs metadata only, never raw private payload unless explicitly enabled

# 19. Failure model

Return explicit machine-readable errors:

* `unsupported_modality`
* `unsupported_route`
* `processor_failed`
* `video_decode_failed`
* `audio_decode_failed`
* `model_load_failed`
* `adapter_parse_failed`
* `tool_schema_invalid`
* `backend_unavailable`

Never let failures masquerade as empty outputs.

# 20. Deployment model

## 20.1 Recommended

* one runner container image
* model-specific config mount
* one model per container
* gateway routes by model name to backend URL
* sidecar or shared utility container for ffmpeg/ocr

## 20.2 Why one model per container

* simpler VRAM accounting
* simpler restarts
* simpler health checks
* simpler failure isolation
* cleaner gateway routing

vLLM itself defaults to one served model per server instance, which is a good operational baseline to preserve. ([vLLM][6])

# 21. Health and readiness

Implement:

* `GET /healthz`
* `GET /readyz`
* `GET /livez`
* `GET /metrics`
* `GET /aether/v1/capabilities`
* `GET /aether/v1/assets/{id}` metadata only

Readiness must fail until:

* model loaded,
* processor ready,
* media toolchain ready,
* manifest registered.

# 22. Recommended build plan

## Phase 0: interface and schema

* request/response schemas
* canonical IR
* capability manifest
* auth middleware
* `/v1/models`
* `/healthz`, `/readyz`

## Phase 1: text + image

* `Gemma4Adapter`
* `POST /v1/chat/completions`
* `POST /v1/responses`
* image ingest
* frame extraction for video-as-frames
* streaming text

## Phase 1.5: audio in

* `POST /v1/audio/transcriptions`
* `POST /v1/audio/translations`
* VAD/segmenter
* E2B/E4B adapter support
* audio-first multimodal prompt packaging

## Phase 2: audio out + video route

* `POST /v1/audio/speech`
* `POST /aether/v1/video/understand`
* TTS adapter abstraction
* ASR + LLM + TTS internal pipelines

## Phase 3: realtime

* WS realtime path
* partial ASR deltas
* partial response deltas
* optional duplex audio

## Phase 4: extra adapters

* Phi
* new Gemini/Gemma variants
* any-to-any families
* research model families

# 23. First implementation target

Do not start with everything.
Start with the narrowest high-ROI slice:

**Build v1 for Gemma 4 E2B/E4B and 26B/31B using a Transformers-native backend with a mandatory multimodal preprocessor and OpenAI-compatible routes for models/chat/responses/transcriptions/translations/speech.**

That gives you:

* immediate utility,
* direct pain relief,
* and a reusable lane for every future model that misses vLLM support on day one.

# 24. First task for Codex

Give Codex this exact first deliverable:

**Task 1: Scaffold Aether Runner v1**

* FastAPI app
* bearer auth middleware
* `/healthz`, `/readyz`, `/v1/models`
* canonical request/response schemas
* `CapabilityManifest`
* `ModelAdapter` interface
* `MediaAsset`, `MediaIngestService`, `VideoFrameExtractor`, `AudioNormalizer`
* `Gemma4Adapter` skeleton
* `POST /v1/chat/completions`
* `POST /v1/responses`
* `POST /v1/audio/transcriptions`
* `POST /v1/audio/translations`
* stub `POST /v1/audio/speech`
* config-driven model registry
* streaming text SSE support
* structured JSON logs
* unit tests for schema normalization and capability checks

# 25. Final call

Yes, build it.

You’ve crossed the threshold where this is no longer “special shit for one model.”
It is now a **missing layer in your stack**.

If you want, next turn I’ll convert this into a cleaner **engineering RFC for Codex** with sections like:

* Goals
* Non-goals
* API contracts
* Internal schemas
* Adapter interface
* Milestones
* Acceptance criteria

[1]: https://docs.vllm.ai/en/stable/serving/openai_compatible_server/?utm_source=chatgpt.com "OpenAI-Compatible Server - vLLM"
[2]: https://developers.openai.com/api/docs/guides/realtime/?utm_source=chatgpt.com "Realtime API"
[3]: https://developers.openai.com/api/docs/guides/migrate-to-responses/?utm_source=chatgpt.com "Migrate to the Responses API"
[4]: https://developers.openai.com/api/docs/guides/speech-to-text/?utm_source=chatgpt.com "Speech to text | OpenAI API"
[5]: https://docs.vllm.ai/en/stable/usage/security/?utm_source=chatgpt.com "Security - vLLM"
[6]: https://docs.vllm.ai/en/v0.19.0/getting_started/quickstart/?utm_source=chatgpt.com "Quickstart - vLLM"

