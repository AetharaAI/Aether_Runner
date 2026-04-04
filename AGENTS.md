# AGENTS.md

## Role
- This repo runs Aether Runner, a Transformers-native fallback inference plane for models that are edge cases for vLLM.
- The responsible agent/operator must keep startup, model loading, auth, and readiness stable on GPU-host deployments.

## Environment
- Repo root: `/home/cory/Aether-Admin-Platform/Aether_Runner`
- Service bind: `http://100.79.252.28:8001` (from compose `.env`)
- Container port: `8000` (published to host port `8001`)
- Model mount in container: `/models` from host `/mnt/aetherpro-extra1/models`
- Git remote: `git@github.com:AetharaAI/Aether_Runner.git`

## Current Mission
- Keep one reliable model path working for `gemma-4-31b-it` through the Transformers backend.
- Prevent startup crash loops by failing clearly on path/config errors.
- Keep health/readiness routes stable for compose deployment.

## Operating Rules
- Work from observed truth, not assumptions.
- Verify claims with commands, logs, tests, or direct inspection.
- If docs conflict with runtime/code, trust runtime/code and update docs.
- No secrets in commits, docs, or logs.
- Make minimal, reversible changes and verify before claiming success.

## VM Workflow Policy (Mandatory)
- VM is pull-and-run only for this repo.
- Do not make manual source edits on the VM copy.
- All source/config changes must be made in this local repo with Codex, then committed, pushed, and pulled on VM.
- If a runtime fix appears to require VM-side source editing, stop and implement that fix in this repo instead.

## Canonical Docs
- `AGENTS.md`
- `PROJECT_STATE.md`
- `CHANGELOG.md`
- `TRUTH.md`

## Known Production Facts
- Compose service name and container name are `gemma-4-31b-it`.
- Inference dependencies are controlled by `INSTALL_INFERENCE` in `.env`.
- Healthcheck calls `GET /v1/models` with bearer token.

## Known Gaps
- Model boot has been blocked by local path mismatches and tokenizer/processor fallback issues.
- vLLM status for Gemma-4 support should be checked periodically against upstream docs/releases.

## Standard Workflow
1. Verify current branch, status, and runtime/log truth.
2. Implement source/config fix in this repo only.
3. Update canonical docs when behavior or operational truth changes.
4. Run tests and config checks.
5. Commit/push, then pull/restart on VM and verify logs/readiness.
