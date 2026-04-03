from __future__ import annotations

from typing import Any

from fastapi import HTTPException


class RunnerError(HTTPException):
    def __init__(self, code: str, message: str, status_code: int = 400, extra: dict[str, Any] | None = None):
        detail: dict[str, Any] = {"error": {"code": code, "message": message}}
        if extra:
            detail["error"]["extra"] = extra
        super().__init__(status_code=status_code, detail=detail)


def unsupported_modality(modality: str, model: str) -> RunnerError:
    return RunnerError(
        code="unsupported_modality",
        message=f"Model '{model}' does not support modality '{modality}'.",
        status_code=400,
    )


def unsupported_route(route: str, model: str) -> RunnerError:
    return RunnerError(
        code="unsupported_route",
        message=f"Model '{model}' does not support route '{route}'.",
        status_code=400,
    )
