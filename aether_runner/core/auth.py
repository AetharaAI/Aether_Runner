from __future__ import annotations

from fastapi import Depends, Header

from aether_runner.core.config import Settings
from aether_runner.core.errors import RunnerError


def require_bearer(settings: Settings):
    def _verify(authorization: str | None = Header(default=None)) -> None:
        if not authorization or not authorization.lower().startswith("bearer "):
            raise RunnerError("unauthorized", "Missing bearer token.", status_code=401)
        token = authorization.split(" ", 1)[1].strip()
        if token not in settings.parsed_api_keys:
            raise RunnerError("unauthorized", "Invalid bearer token.", status_code=401)

    return _verify


def auth_dependency(settings: Settings):
    return Depends(require_bearer(settings))
