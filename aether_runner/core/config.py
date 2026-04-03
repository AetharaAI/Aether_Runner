from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelDefaults(BaseModel):
    temperature: float = 1.0
    top_p: float = 0.95
    top_k: int = 64
    max_output_tokens: int = 1024
    enable_thinking: bool = False
    vision_token_budget: int = 280


class ModelSupports(BaseModel):
    text: bool = True
    image: bool = False
    audio: bool = False
    video: bool = False
    tools: bool = False
    responses: bool = True
    chat: bool = True
    embeddings: bool = False
    transcription: bool = False
    translation: bool = False
    tts: bool = False


class ModelConfig(BaseModel):
    id: str
    path: str
    adapter: str
    backend: str = "transformers"
    dtype: str = "auto"
    device_map: str = "auto"
    trust_remote_code: bool = False
    max_context_tokens: int = 32768
    supports: ModelSupports = Field(default_factory=ModelSupports)
    defaults: ModelDefaults = Field(default_factory=ModelDefaults)


class RunnerMaxUpload(BaseModel):
    image: int = 50
    audio: int = 200
    video: int = 1000


class RunnerConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8010
    auth_mode: str = "bearer"
    temp_dir: str = "/tmp/aether-runner"
    media_cache_dir: str = "/cache/media"
    asset_ttl_seconds: int = 86400
    max_upload_mb: RunnerMaxUpload = Field(default_factory=RunnerMaxUpload)
    enable_realtime: bool = False
    allow_remote_urls: bool = False
    max_request_mb: int = 128


class RunnerFileConfig(BaseModel):
    runner: RunnerConfig
    models: list[ModelConfig]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="AETHER_", case_sensitive=False)

    config_path: str = "config/runner.yaml"
    api_keys: str = "dev-secret-key"
    log_level: str = "INFO"
    allow_private_urls: bool = False
    eager_model_load: bool = False

    @property
    def parsed_api_keys(self) -> set[str]:
        return {k.strip() for k in self.api_keys.split(",") if k.strip()}


def load_runner_file(path: str) -> RunnerFileConfig:
    cfg_path = Path(path)
    data: dict[str, Any] = yaml.safe_load(cfg_path.read_text())
    return RunnerFileConfig.model_validate(data)
