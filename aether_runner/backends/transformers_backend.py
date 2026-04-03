from __future__ import annotations

import importlib
from typing import Any


class TransformersBackend:
    """Lazy transformers backend wrapper.

    This keeps startup lightweight for environments without torch/transformers.
    """

    def __init__(self, model_path: str, dtype: str = "auto", device_map: str = "auto", trust_remote_code: bool = False):
        self.model_path = model_path
        self.dtype = dtype
        self.device_map = device_map
        self.trust_remote_code = trust_remote_code
        self._processor: Any | None = None
        self._model: Any | None = None
        self._loaded = False

    @property
    def loaded(self) -> bool:
        return self._loaded

    def load(self) -> None:
        transformers = importlib.import_module("transformers")
        torch = importlib.import_module("torch")

        auto_processor = getattr(transformers, "AutoProcessor")
        auto_model = getattr(transformers, "AutoModelForCausalLM")

        self._processor = auto_processor.from_pretrained(self.model_path, trust_remote_code=self.trust_remote_code)
        torch_dtype = getattr(torch, self.dtype, "auto") if self.dtype != "auto" else "auto"
        self._model = auto_model.from_pretrained(
            self.model_path,
            trust_remote_code=self.trust_remote_code,
            torch_dtype=torch_dtype,
            device_map=self.device_map,
        )
        self._loaded = True

    def generate_text(self, prompt: str, max_new_tokens: int = 256, temperature: float = 1.0, top_p: float = 0.95) -> str:
        if not self._loaded:
            raise RuntimeError("backend_unavailable: transformers backend not loaded")
        # A minimal generic generate implementation. Family adapters can override for better behavior.
        inputs = self._processor(text=prompt, return_tensors="pt")
        outputs = self._model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=temperature > 0,
            temperature=max(temperature, 1e-5),
            top_p=top_p,
        )
        decoded = self._processor.batch_decode(outputs, skip_special_tokens=True)
        return decoded[0] if decoded else ""
