from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field

from prometheus_client import Counter, Histogram


REQUEST_COUNT = Counter("aether_requests_total", "Total requests", ["route", "status"])
REQUEST_LATENCY = Histogram("aether_request_latency_seconds", "Request latency", ["route"])
PREPROCESS_LATENCY = Histogram("aether_preprocess_latency_seconds", "Preprocess latency", ["route"])
MODEL_LATENCY = Histogram("aether_model_latency_seconds", "Model latency", ["route", "model"])


@dataclass
class RequestTelemetry:
    preprocess_ms: float = 0
    model_ms: float = 0
    total_ms: float = 0
    input_tokens: int = 0
    output_tokens: int = 0
    frame_count: int = 0
    audio_seconds: float = 0
    cache_hit: bool = False
    extras: dict[str, float] = field(default_factory=dict)


class InMemoryMetrics:
    def __init__(self) -> None:
        self.route_errors: dict[str, int] = defaultdict(int)

    def record_error(self, route: str) -> None:
        self.route_errors[route] += 1
