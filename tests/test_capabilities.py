from aether_runner.core.config import load_runner_file
from aether_runner.models.schemas import ModelsConfigValidation
from aether_runner.services.model_registry import ModelRegistry


def test_registry_loads_and_has_models() -> None:
    cfg = load_runner_file("config/runner.yaml")
    registry = ModelRegistry(cfg, eager_load=False)
    registry.load()
    manifests = registry.list_manifests()
    assert len(manifests) >= 2
    assert any(m.id == "gemma-4-e4b-it" for m in manifests)


def test_capabilities_unique_ids_validation() -> None:
    cfg = load_runner_file("config/runner.yaml")
    registry = ModelRegistry(cfg, eager_load=False)
    registry.load()
    manifests = registry.list_manifests()
    ModelsConfigValidation(models=manifests)
