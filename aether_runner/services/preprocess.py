from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter
from typing import Any

from aether_runner.models.schemas import CanonicalRequest, MediaAsset
from aether_runner.services.assets import AssetRegistry
from aether_runner.services.audio import AudioNormalizer, Diarizer, VADSegmenter
from aether_runner.services.image import ImageNormalizer
from aether_runner.services.video import VideoFrameExtractor


@dataclass
class PreprocessResult:
    assets: list[MediaAsset]
    plan: dict[str, Any]
    token_estimate: int
    preprocess_ms: float


class MultimodalPreprocessor:
    def __init__(self, registry: AssetRegistry):
        self.registry = registry
        self.audio = AudioNormalizer()
        self.vad = VADSegmenter()
        self.diarizer = Diarizer()
        self.image = ImageNormalizer()
        self.video = VideoFrameExtractor()

    def _collect_assets(self, req: CanonicalRequest) -> list[MediaAsset]:
        assets: list[MediaAsset] = []
        for msg in req.messages:
            if isinstance(msg.content, list):
                for item in msg.content:
                    if item.asset_id:
                        asset = self.registry.maybe_get(item.asset_id)
                        if asset:
                            assets.append(asset)
        for bucket in ("audio", "images", "video"):
            for media_ref in req.media.get(bucket, []):
                asset_id = media_ref.get("asset_id")
                if asset_id:
                    asset = self.registry.maybe_get(asset_id)
                    if asset:
                        assets.append(asset)
        # dedupe while preserving order
        seen: set[str] = set()
        uniq: list[MediaAsset] = []
        for a in assets:
            if a.asset_id not in seen:
                seen.add(a.asset_id)
                uniq.append(a)
        return uniq

    def _enrich_asset(self, asset: MediaAsset) -> dict[str, Any]:
        if asset.modality == "audio":
            norm = self.audio.normalize(asset.path)
            return {
                "asset_id": asset.asset_id,
                "modality": "audio",
                "metadata": norm,
                "vad": self.vad.segment(asset.path),
                "diarization": self.diarizer.diarize(asset.path),
            }
        if asset.modality == "image":
            return {
                "asset_id": asset.asset_id,
                "modality": "image",
                "metadata": self.image.normalize(asset.path),
            }
        if asset.modality == "video":
            return {
                "asset_id": asset.asset_id,
                "modality": "video",
                "metadata": self.video.extract(asset.path),
            }
        return {
            "asset_id": asset.asset_id,
            "modality": asset.modality,
            "metadata": asset.metadata,
        }

    def process(self, req: CanonicalRequest, capabilities_modalities: set[str]) -> PreprocessResult:
        started = perf_counter()
        assets = self._collect_assets(req)
        enriched = [self._enrich_asset(a) for a in assets]
        modalities = req.modalities()

        plan: dict[str, Any] = {
            "modalities": sorted(modalities),
            "assets": enriched,
            "steps": [],
        }
        if "video" in modalities:
            plan["steps"].append("video_as_frames")
        if "audio" in modalities:
            plan["steps"].append("audio_task")
        if "image" in modalities:
            plan["steps"].append("vision_direct")
        plan["steps"].append("prompt_package")

        unsupported = [m for m in modalities if m not in capabilities_modalities]
        if unsupported:
            plan["unsupported"] = unsupported

        text_chars = sum(len(str(m.content)) for m in req.messages)
        token_estimate = max(1, text_chars // 4)
        preprocess_ms = (perf_counter() - started) * 1000.0
        return PreprocessResult(assets=assets, plan=plan, token_estimate=token_estimate, preprocess_ms=preprocess_ms)
