from __future__ import annotations

from pathlib import Path


class VideoFrameExtractor:
    def extract(self, path: str, fps: int = 1, frame_budget: int = 32) -> dict[str, int | str | list[str]]:
        # Placeholder implementation for v1 scaffold.
        # On GPU/production hosts, wire ffmpeg extraction here.
        p = Path(path)
        return {
            "source": str(p),
            "fps": fps,
            "frame_count": 0,
            "frame_budget": frame_budget,
            "frames": [],
        }


class VideoSampler:
    def plan(self, duration_seconds: float, fps: int, frame_budget: int) -> dict[str, int | float]:
        planned = min(frame_budget, max(1, int(duration_seconds * fps)))
        return {"duration_seconds": duration_seconds, "fps": fps, "planned_frames": planned}
