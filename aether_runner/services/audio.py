from __future__ import annotations

import wave
from pathlib import Path


class AudioNormalizer:
    def __init__(self, target_sample_rate: int = 16000):
        self.target_sample_rate = target_sample_rate

    def normalize(self, path: str) -> dict[str, float | int | str]:
        p = Path(path)
        metadata: dict[str, float | int | str] = {
            "path": str(p),
            "sample_rate": self.target_sample_rate,
            "channels": 1,
            "seconds": 0.0,
            "normalized": False,
        }
        if p.suffix.lower() == ".wav":
            try:
                with wave.open(str(p), "rb") as wf:
                    frames = wf.getnframes()
                    rate = wf.getframerate() or self.target_sample_rate
                    metadata["sample_rate"] = rate
                    metadata["channels"] = wf.getnchannels()
                    metadata["seconds"] = round(frames / float(rate), 4)
                    metadata["normalized"] = True
            except Exception:
                # Fail soft in v1 scaffold to keep endpoint behavior explicit and resilient.
                metadata["normalized"] = False
        return metadata


class VADSegmenter:
    def segment(self, path: str) -> list[dict[str, float]]:
        # Placeholder VAD segmentation. Integrate pyannote/silero in production.
        return [{"start": 0.0, "end": 0.0, "confidence": 0.0}]


class Diarizer:
    def diarize(self, path: str) -> list[dict[str, float | str]]:
        return []
