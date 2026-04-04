# TRUTH.md

## Identity
- Project name: `Aether_Runner`
- Purpose: Transformers-native fallback inference plane for OpenAI-compatible and Aether multimodal routes.
- Frontend repo: N/A (API service repo)
- Backend repo: `AetharaAI/Aether_Runner`

## Runtime
- Public URL: `http://100.79.252.28:8001`
- API URL: `http://100.79.252.28:8001/v1`
- Repo root: `/home/cory/Aether-Admin-Platform/Aether_Runner`
- Deploy path (VM): `~/aether-model-node/control/Aether_Runner`

## Infra
- Provider: OVHcloud (operator-supplied standing fact)
- Region: `us-west-or-1` (observed from VM hostname context)
- Instance type: `L40S-180` (operator-supplied standing fact)
- Tailscale IP: `100.79.252.28`

## Current Production Truth
- The running target model for this repo is `gemma-4-31b-it` via Transformers backend.
- Model weights are expected in mounted container path `/models/google/gemma-4-31B-it`.
- Compose service publishes container `:8000` to host `:8001`.

## Operator Mechanics
- Build command: `docker compose up -d --build`
- Restart command: `docker compose down && docker compose up -d --build`
- Verification command/path: `docker compose logs -f --tail=200` and `GET /v1/models`
- Active working branch: `main` (current repo state)
- Main branch policy: `main` is stable, clean, and deployable
- Checkpoint merge rule: merge to `main` only at validated checkpoint stages
- Checkpoint tag convention: `checkpoint-YYYYMMDD-<short-topic>`
- Post-checkpoint rule: return to working branch after merge/tag
- Reference: `TRUTH/GIT-WORKFLOW-DISCIPLINE.md`

## Operator Profile Reference
- Reference: `TRUTH/OPERATOR_PROFILE.md`
- Use when operator identity, preferences, or standing company facts materially affect execution.

## Ownership
- Responsible operator: Cory Gibson
- Responsible coding agent: Codex
