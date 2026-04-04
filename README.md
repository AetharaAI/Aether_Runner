# Aether Runner

Aether Runner is a Transformers-native fallback inference plane for edge-case and multimodal models that are not production-ready in vLLM yet. It exposes OpenAI-compatible routes plus Aether-native multimodal/debug routes.

## What is implemented (v1 scaffold)

- FastAPI service with bearer auth on all routes
- OpenAI-compatible routes:
  - `GET /v1/models`
  - `POST /v1/chat/completions` (SSE streaming supported)
  - `POST /v1/responses` (SSE streaming supported)
  - `POST /v1/completions`
  - `POST /v1/audio/transcriptions`
  - `POST /v1/audio/translations`
  - `POST /v1/audio/speech` (explicit backend stub)
- Aether routes:
  - `GET /aether/v1/capabilities`
  - `POST /aether/v1/media/ingest`
  - `POST /aether/v1/mm/parse`
  - `POST /aether/v1/video/understand`
  - `GET /aether/v1/assets/{id}`
- Mandatory multimodal preprocess path (asset collection, normalization skeletons, modality planning)
- Adapter architecture with `ModelAdapter` protocol and first adapters:
  - `Gemma4Adapter`
  - `GenericHFChatAdapter`
- Config-driven model registry and capability manifests
- JSON structured logging + Prometheus metrics endpoint
- Unit tests for normalization, capability registration, auth, and route baseline

## Project layout

- `aether_runner/main.py`: app bootstrap, middleware, error handling
- `aether_runner/api/routes.py`: OpenAI + Aether endpoints
- `aether_runner/models/schemas.py`: canonical IR and API schemas
- `aether_runner/services/model_registry.py`: adapter/model registry
- `aether_runner/services/preprocess.py`: multimodal preprocessor
- `aether_runner/services/media_ingest.py`: ingest service with URL safety checks
- `aether_runner/adapters/`: adapter protocol and implementations
- `aether_runner/backends/transformers_backend.py`: lazy Transformers backend
- `config/runner.yaml`: runner + model definitions

## Local run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn aether_runner.main:app --host 0.0.0.0 --port 8010
```

Request auth header for all endpoints:

```text
Authorization: Bearer <your-aether-api-key>
```

## Docker Compose run

```bash
docker compose up --build
```

Then run smoke test:

```bash
./scripts/smoke.sh
```

## GPU deployment notes for your Gemma host

1. Install optional inference deps in image/host:
   - set `INSTALL_INFERENCE=true` in `.env` (compose will install `torch`, `transformers`, `accelerate`)
2. Mount model weights into the container and update `config/runner.yaml` model `path`.
3. Set `AETHER_EAGER_MODEL_LOAD=true` to fail-fast on startup if the model cannot load.
4. For NVIDIA hosts, enable GPU in compose by uncommenting the `deploy.resources...devices` block.

## Example calls

List models:

```bash
curl -H "Authorization: Bearer <your-aether-api-key>" http://localhost:8010/v1/models
```

Chat completion:

```bash
curl -H "Authorization: Bearer <your-aether-api-key>" \
  -H "Content-Type: application/json" \
  -d '{
    "model":"gemma-4-31b-it",
    "messages":[{"role":"user","content":[{"type":"text","text":"hello"}]}]
  }' \
  http://localhost:8010/v1/chat/completions
```

Media ingest:

```bash
curl -H "Authorization: Bearer <your-aether-api-key>" \
  -F file=@./sample.wav \
  http://localhost:8010/aether/v1/media/ingest
```

## Notes

- This repo is intentionally model-agnostic; adding a new model family is done by adding an adapter and a config entry.
- Audio/video endpoints are wired and capability-validated. ASR/TTS/video heavy lifting is scaffolded with explicit placeholders where backend engines should be attached.
