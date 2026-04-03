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
        self._tokenizer: Any | None = None
        self._model: Any | None = None
        self._loaded = False

    @property
    def loaded(self) -> bool:
        return self._loaded

    def load(self) -> None:
        transformers = importlib.import_module("transformers")
        torch = importlib.import_module("torch")

        auto_processor = getattr(transformers, "AutoProcessor")
        auto_tokenizer = getattr(transformers, "AutoTokenizer")
        auto_model = getattr(transformers, "AutoModelForCausalLM")

        try:
            self._processor = auto_processor.from_pretrained(
                self.model_path,
                trust_remote_code=self.trust_remote_code,
            )
        except Exception:
            # Some quantized/exported bundles do not include a usable multimodal processor.
            # Fall back to tokenizer-only mode for text generation compatibility.
            try:
                # Prefer fast tokenizer first (often works with tokenizer.json-only exports).
                self._tokenizer = auto_tokenizer.from_pretrained(
                    self.model_path,
                    trust_remote_code=self.trust_remote_code,
                    use_fast=True,
                )
            except Exception:
                # Fallback to slow tokenizer as a last resort.
                self._tokenizer = auto_tokenizer.from_pretrained(
                    self.model_path,
                    trust_remote_code=self.trust_remote_code,
                    use_fast=False,
                )

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
        if self._processor is not None:
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

        if self._tokenizer is None:
            raise RuntimeError("backend_unavailable: neither processor nor tokenizer is available")

        inputs = self._tokenizer(prompt, return_tensors="pt")
        model_device = getattr(self._model, "device", None)
        if model_device is not None:
            inputs = {k: v.to(model_device) for k, v in inputs.items()}
        outputs = self._model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=temperature > 0,
            temperature=max(temperature, 1e-5),
            top_p=top_p,
        )
        decoded = self._tokenizer.batch_decode(outputs, skip_special_tokens=True)
        return decoded[0] if decoded else ""
