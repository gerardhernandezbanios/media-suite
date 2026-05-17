# services/backend/app/media/infrastructure/hashing/sha256.py
from __future__ import annotations

import hashlib
from pathlib import Path

from app.media.domain.services import HashCalculator
from app.media.infrastructure.hashing.perceptual import compute_phash


class DefaultHashCalculator(HashCalculator):
    def sha256(self, path: Path) -> str:
        h = hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()

    def phash(self, path: Path) -> str | None:
        return compute_phash(path)
