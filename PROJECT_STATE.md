# PROJECT_STATE.md

## Repo
- Name: `Aether_Runner`
- Root: `/home/cory/Aether-Admin-Platform/Aether_Runner`
- Public URL target: `http://100.79.252.28:8001`
- Deploy target: VM path `~/aether-model-node/control/Aether_Runner` with `docker compose`
- GitHub remote: `git@github.com:AetharaAI/Aether_Runner.git`

## Production Status
- API scaffold, auth, routes, registry, and adapter framework are implemented.
- Active deployment objective is stable boot/readiness for `gemma-4-31b-it` on L40S through Transformers backend.
- Most recent blocker observed on VM: local model path mismatch/case mismatch caused startup failure.

## Deploy Reality
- Compose service: `gemma-4-31b-it`
- Mounted model root: `/models` from `/mnt/aetherpro-extra1/models`
- Required model directory for current config: `/models/google/gemma-4-31B-it`
- Inference dependency toggle: `INSTALL_INFERENCE` in `.env`

## Repo Alignment Status
- Source-of-truth edits must happen in this local repo and flow to VM via push/pull only.
- VM source edits are explicitly disallowed by policy in `AGENTS.md`.

## Dependencies
- Python runtime in container (`python:3.11-slim`)
- `torch`, `transformers`, `accelerate`, `sentencepiece`, `protobuf` when inference deps are enabled
- NVIDIA runtime + GPU device mapping in compose

## Remaining Gaps
- End-to-end verified successful model load on VM still pending after path/case correction.
- Additional hardening may be needed for Gemma-specific processor/tokenizer edge cases after first clean boot.

## Key Files
- `config/runner.yaml`
- `docker-compose.yml`
- `aether_runner/backends/transformers_backend.py`
- `aether_runner/adapters/gemma4.py`
- `aether_runner/services/model_registry.py`
- `.env` and `.env.example`

## Next Steps
1. Pull latest commit on VM, rebuild, and verify container boot without restart loop.
2. Verify readiness/auth path via `GET /v1/models` and capture the first clean log segment in `logs/VM-error-logs.md` (or rename once clean).
