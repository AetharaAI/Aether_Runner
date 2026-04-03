#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${BASE_URL:-http://localhost:8010}"
KEY="${AETHER_KEY:-}"
if [ -z "${KEY}" ]; then
  echo "AETHER_KEY must be set" >&2
  exit 1
fi

curl -sf -H "Authorization: Bearer ${KEY}" "${BASE_URL}/healthz" >/dev/null
curl -sf -H "Authorization: Bearer ${KEY}" "${BASE_URL}/readyz" >/dev/null
curl -sf -H "Authorization: Bearer ${KEY}" "${BASE_URL}/v1/models" | jq . >/dev/null

curl -sf -H "Authorization: Bearer ${KEY}" -H 'content-type: application/json' \
  -d '{"model":"generic-hf-chat","messages":[{"role":"user","content":[{"type":"text","text":"hello"}]}]}' \
  "${BASE_URL}/v1/chat/completions" | jq . >/dev/null

echo "smoke: ok"
