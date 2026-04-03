from __future__ import annotations

import hashlib
import mimetypes
import shutil
import uuid
from pathlib import Path

from aether_runner.models.schemas import MediaAsset


class MediaCache:
    def __init__(self) -> None:
        self._sha_to_id: dict[str, str] = {}

    def find(self, sha256: str) -> str | None:
        return self._sha_to_id.get(sha256)

    def put(self, sha256: str, asset_id: str) -> None:
        self._sha_to_id[sha256] = asset_id


class AssetRegistry:
    def __init__(self, root: str):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self._assets: dict[str, MediaAsset] = {}
        self.cache = MediaCache()

    def _hash_file(self, path: Path) -> str:
        h = hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
        return h.hexdigest()

    def _modality_for_mime(self, mime_type: str) -> str:
        if mime_type.startswith("image/"):
            return "image"
        if mime_type.startswith("audio/"):
            return "audio"
        if mime_type.startswith("video/"):
            return "video"
        if mime_type in {"application/pdf"}:
            return "document"
        if mime_type.startswith("text/"):
            return "text"
        return "unknown"

    def register_file(self, src_path: Path, original_name: str | None = None) -> MediaAsset:
        sha = self._hash_file(src_path)
        existing = self.cache.find(sha)
        if existing:
            return self._assets[existing]

        asset_id = f"asset_{uuid.uuid4().hex[:16]}"
        ext = Path(original_name or src_path.name).suffix or ".bin"
        dst = self.root / f"{asset_id}{ext}"
        shutil.copy2(src_path, dst)

        mime = mimetypes.guess_type(dst.name)[0] or "application/octet-stream"
        size = dst.stat().st_size
        asset = MediaAsset(
            asset_id=asset_id,
            sha256=sha,
            path=str(dst),
            mime_type=mime,
            size_bytes=size,
            modality=self._modality_for_mime(mime),
        )
        self._assets[asset_id] = asset
        self.cache.put(sha, asset_id)
        return asset

    def register_bytes(self, payload: bytes, filename: str = "upload.bin") -> MediaAsset:
        tmp = self.root / f"tmp_{uuid.uuid4().hex}"
        tmp.write_bytes(payload)
        try:
            return self.register_file(tmp, original_name=filename)
        finally:
            if tmp.exists():
                tmp.unlink()

    def get(self, asset_id: str) -> MediaAsset:
        return self._assets[asset_id]

    def maybe_get(self, asset_id: str) -> MediaAsset | None:
        return self._assets.get(asset_id)

    def list_assets(self) -> list[MediaAsset]:
        return list(self._assets.values())
