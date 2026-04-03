from __future__ import annotations

import logging
import time

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from aether_runner.api.routes import build_router
from aether_runner.core.config import Settings, load_runner_file
from aether_runner.core.errors import RunnerError
from aether_runner.core.logging import configure_logging
from aether_runner.core.metrics import REQUEST_COUNT, REQUEST_LATENCY
from aether_runner.services.assets import AssetRegistry
from aether_runner.services.executor import RunnerExecutor
from aether_runner.services.media_ingest import MediaIngestService
from aether_runner.services.model_registry import ModelRegistry
from aether_runner.services.preprocess import MultimodalPreprocessor


settings = Settings()
configure_logging(settings.log_level)
logger = logging.getLogger(__name__)

if not settings.parsed_api_keys:
    raise RuntimeError("AETHER_API_KEYS must be set with at least one bearer token.")

file_cfg = load_runner_file(settings.config_path)
asset_registry = AssetRegistry(file_cfg.runner.media_cache_dir)
model_registry = ModelRegistry(file_cfg, eager_load=settings.eager_model_load)
model_registry.load()

preprocessor = MultimodalPreprocessor(asset_registry)
executor = RunnerExecutor(preprocessor)
ingest = MediaIngestService(asset_registry, settings)

app = FastAPI(
    title="Aether Runner",
    version="0.1.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)
app.include_router(build_router(settings, model_registry, ingest, executor))


@app.middleware("http")
async def request_limit_middleware(request: Request, call_next):
    max_bytes = file_cfg.runner.max_request_mb * 1024 * 1024
    content_length = request.headers.get("content-length")
    if content_length and int(content_length) > max_bytes:
        return JSONResponse(
            status_code=413,
            content={
                "error": {
                    "code": "request_too_large",
                    "message": f"Request exceeds max_request_mb={file_cfg.runner.max_request_mb}",
                }
            },
        )
    return await call_next(request)


@app.middleware("http")
async def timing_middleware(request: Request, call_next):
    started = time.perf_counter()
    try:
        response = await call_next(request)
        status = str(response.status_code)
    except Exception:
        REQUEST_COUNT.labels(route=request.url.path, status="500").inc()
        REQUEST_LATENCY.labels(route=request.url.path).observe(time.perf_counter() - started)
        raise
    REQUEST_COUNT.labels(route=request.url.path, status=status).inc()
    REQUEST_LATENCY.labels(route=request.url.path).observe(time.perf_counter() - started)
    return response


@app.exception_handler(RunnerError)
async def runner_error_handler(_: Request, exc: RunnerError):
    logger.warning(
        "runner_error",
        extra={"error_stage": "request", "exception_class": exc.__class__.__name__},
    )
    return JSONResponse(status_code=exc.status_code, content=exc.detail)


@app.exception_handler(Exception)
async def generic_error_handler(_: Request, exc: Exception):
    logger.exception("unhandled_error")
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": "internal_error",
                "message": str(exc),
            }
        },
    )
