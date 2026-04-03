import os
from fastapi.testclient import TestClient

os.environ.setdefault("AETHER_API_KEYS", "test-key")
from aether_runner.main import app


client = TestClient(app)


def _headers(token: str = "test-key") -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def test_auth_required() -> None:
    response = client.get("/healthz")
    assert response.status_code == 401


def test_models_route_available() -> None:
    response = client.get("/v1/models", headers=_headers())
    assert response.status_code == 200
    data = response.json()
    assert data["object"] == "list"
    assert len(data["data"]) >= 1


def test_chat_completion_works() -> None:
    payload = {
        "model": "generic-hf-chat",
        "messages": [{"role": "user", "content": [{"type": "text", "text": "hello"}]}],
        "stream": False,
    }
    response = client.post("/v1/chat/completions", headers=_headers(), json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["object"] == "chat.completion"
    assert body["choices"][0]["message"]["role"] == "assistant"
