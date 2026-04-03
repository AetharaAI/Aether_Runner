from __future__ import annotations

import base64
import ipaddress
import socket
import tempfile
from pathlib import Path
from urllib.parse import urlparse

import httpx

from aether_runner.core.config import Settings
from aether_runner.core.errors import RunnerError
from aether_runner.models.schemas import MediaAsset
from aether_runner.services.assets import AssetRegistry


class MediaIngestService:
    def __init__(self, registry: AssetRegistry, settings: Settings):
        self.registry = registry
        self.settings = settings

    def ingest_bytes(self, payload: bytes, filename: str) -> MediaAsset:
        if not payload:
            raise RunnerError("asset_ingest_failed", "Received empty payload.", status_code=400)
        return self.registry.register_bytes(payload, filename=filename)

    def ingest_base64(self, b64_data: str, filename: str = "upload.bin") -> MediaAsset:
        try:
            payload = base64.b64decode(b64_data)
        except Exception as exc:
            raise RunnerError("asset_ingest_failed", "Invalid base64 payload.", status_code=400) from exc
        return self.ingest_bytes(payload, filename)

    def ingest_path(self, path: str) -> MediaAsset:
        p = Path(path)
        if not p.exists() or not p.is_file():
            raise RunnerError("asset_ingest_failed", f"Path not found: {path}", status_code=400)
        return self.registry.register_file(p, original_name=p.name)

    def _is_private_host(self, hostname: str) -> bool:
        try:
            ip = ipaddress.ip_address(socket.gethostbyname(hostname))
            return ip.is_private or ip.is_loopback or ip.is_link_local
        except Exception:
            return True

    def ingest_url(self, url: str) -> MediaAsset:
        if not url.lower().startswith(("http://", "https://")):
            raise RunnerError("asset_ingest_failed", "Only http/https URLs are allowed.", status_code=400)

        parsed = urlparse(url)
        if not parsed.hostname:
            raise RunnerError("asset_ingest_failed", "Invalid URL host.", status_code=400)

        if self._is_private_host(parsed.hostname) and not self.settings.allow_private_urls:
            raise RunnerError("asset_ingest_failed", "Blocked private/loopback URL.", status_code=403)

        try:
            with httpx.Client(timeout=15.0, follow_redirects=True) as client:
                response = client.get(url)
                response.raise_for_status()
                payload = response.content
            suffix = Path(parsed.path).suffix or ".bin"
            return self.registry.register_bytes(payload, filename=f"remote{suffix}")
        except RunnerError:
            raise
        except Exception as exc:
            raise RunnerError("asset_ingest_failed", f"Failed to fetch URL: {exc}", status_code=400) from exc

    def ingest_upload(self, filename: str, payload: bytes) -> MediaAsset:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(payload)
            tmp_path = Path(tmp.name)
        try:
            return self.registry.register_file(tmp_path, original_name=filename)
        finally:
            if tmp_path.exists():
                tmp_path.unlink()
