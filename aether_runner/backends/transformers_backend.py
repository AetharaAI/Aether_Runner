from __future__ import annotations

import importlib
import json
import tempfile
from typing import Any
from pathlib import Path


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
                # Some AWQ exports carry tokenizer_config shapes that break fast tokenizer init.
                # Patch common issues in a temp copy and retry fast tokenizer.
                self._tokenizer = self._load_patched_fast_tokenizer(auto_tokenizer)

        torch_dtype = getattr(torch, self.dtype, "auto") if self.dtype != "auto" else "auto"
        self._model = auto_model.from_pretrained(
            self.model_path,
            trust_remote_code=self.trust_remote_code,
            torch_dtype=torch_dtype,
            device_map=self.device_map,
        )
        self._loaded = True

    def _load_patched_fast_tokenizer(self, auto_tokenizer: Any) -> Any:
        model_dir = Path(self.model_path)
        tok_cfg = model_dir / "tokenizer_config.json"
        if not tok_cfg.exists():
            raise RuntimeError("backend_unavailable: tokenizer_config.json not found for tokenizer fallback")

        with tempfile.TemporaryDirectory(prefix="aether_tokfix_") as td:
            temp_dir = Path(td)
            # Copy only tokenizer-relevant files to keep patch scope minimal.
            for name in (
                "tokenizer_config.json",
                "tokenizer.json",
                "special_tokens_map.json",
                "config.json",
                "generation_config.json",
            ):
                src = model_dir / name
                if src.exists():
                    (temp_dir / name).write_bytes(src.read_bytes())

            cfg_path = temp_dir / "tokenizer_config.json"
            cfg = json.loads(cfg_path.read_text())

            # HF expects extra_special_tokens as a mapping; some exports write a list.
            extras = cfg.get("extra_special_tokens")
            if isinstance(extras, list):
                cfg["extra_special_tokens"] = {f"extra_token_{i}": tok for i, tok in enumerate(extras)}

            # Prefer tokenizer.json for fast tokenizer path.
            if (temp_dir / "tokenizer.json").exists():
                cfg["tokenizer_file"] = "tokenizer.json"

            cfg_path.write_text(json.dumps(cfg))
            return auto_tokenizer.from_pretrained(
                str(temp_dir),
                trust_remote_code=self.trust_remote_code,
                use_fast=True,
            )

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
