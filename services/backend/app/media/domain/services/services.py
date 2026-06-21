# services/backend/app/media/domain/services.py
from __future__ import annotations

from pathlib import Path
from typing import Optional, Protocol

from app.media.domain.entities import MediaItem
from services.backend.app.media.domain.entities.exif import ExifData


class ExifReader(Protocol):
    def extract(self, path: Path) -> Optional[ExifData]:
        ...


class HashCalculator(Protocol):
    def sha256(self, path: Path) -> str:
        ...

    def phash(self, path: Path) -> Optional[str]:
        ...


class MediaStorage(Protocol):
    def move_to_library(self, src: Path, item: MediaItem) -> Path:
        ...
