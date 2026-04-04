# CHANGELOG.md

## 2026-04-04

### Runtime Stability
- Set active model path to `'/models/google/gemma-4-31B-it'` in `config/runner.yaml` to match observed VM directory case.
- Hardened `TransformersBackend.load()` to detect missing local model directories before Hugging Face repo-id fallback behavior.
- Enabled `local_files_only=True` for local-path model/processor/tokenizer loading paths to avoid hub-validation loops when path is intended to be local.

### Workflow
- Added root `AGENTS.md` with explicit VM policy: no manual source edits on VM, local repo edits only, then push/pull.
- Added canonical root docs: `TRUTH.md`, `PROJECT_STATE.md`, `CHANGELOG.md`.

### Verification
- Pending VM pull/rebuild verification for clean boot and readiness on `gemma-4-31b-it`.
