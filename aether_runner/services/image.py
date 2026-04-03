from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageOps


class ImageNormalizer:
    def normalize(self, path: str) -> dict[str, int | float | str | bool]:
        p = Path(path)
        with Image.open(p) as img:
            fixed = ImageOps.exif_transpose(img).convert("RGB")
            width, height = fixed.size
            return {
                "path": str(p),
                "width": width,
                "height": height,
                "aspect_ratio": round(width / max(height, 1), 4),
                "normalized": True,
            }
