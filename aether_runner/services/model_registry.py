from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from aether_runner.adapters.gemma4 import Gemma4Adapter
from aether_runner.adapters.generic_hf import GenericHFChatAdapter
from aether_runner.core.config import ModelConfig, RunnerFileConfig
from aether_runner.core.errors import RunnerError
from aether_runner.models.schemas import CapabilityManifest


ADAPTER_FACTORIES = {
    "gemma4": Gemma4Adapter,
    "generic_hf_chat": GenericHFChatAdapter,
    "generic_hf": GenericHFChatAdapter,
}


@dataclass
class RegisteredModel:
    cfg: ModelConfig
    adapter: Any
    manifest: CapabilityManifest


class ModelRegistry:
    def __init__(self, cfg: RunnerFileConfig, eager_load: bool = False):
        self.cfg = cfg
        self.eager_load = eager_load
        self._models: dict[str, RegisteredModel] = {}
        self._ready = False

    def load(self) -> None:
        for model_cfg in self.cfg.models:
            factory = ADAPTER_FACTORIES.get(model_cfg.adapter)
            if not factory:
                raise RunnerError("model_load_failed", f"Unknown adapter '{model_cfg.adapter}'", status_code=500)
            adapter = factory(model_cfg)
            if hasattr(adapter, "maybe_load"):
                adapter.maybe_load(eager=self.eager_load)
            manifest = adapter.capabilities()
            self._models[model_cfg.id] = RegisteredModel(cfg=model_cfg, adapter=adapter, manifest=manifest)
        self._ready = True

    def ready(self) -> bool:
        return self._ready

    def list_manifests(self) -> list[CapabilityManifest]:
        return [m.manifest for m in self._models.values()]

    def get(self, model_id: str) -> RegisteredModel:
        found = self._models.get(model_id)
        if not found:
            raise RunnerError("model_not_found", f"Model '{model_id}' not found.", status_code=404)
        return found

    def capabilities_by_model(self) -> dict[str, CapabilityManifest]:
        return {model_id: reg.manifest for model_id, reg in self._models.items()}
