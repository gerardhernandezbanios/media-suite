# services/backend/app/media/infrastructure/filesystem/storage.py
from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path

from app.media.domain.entities import MediaItem
from services.backend.app.media.domain.services.services import MediaStorage


class LibraryMediaStorage(MediaStorage):
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir

    def move_to_library(self, src: Path, item: MediaItem) -> Path:
        created = item.created_at or datetime.utcnow()
        year = f"{created.year:04d}"
        month = f"{created.month:02d}"

        if item.type.name.lower() == "image":
            subdir = "image"
        elif item.type.name.lower() == "video":
            subdir = "video"
        else:
            subdir = "other"

        target_dir = self.base_dir / subdir / year / month
        target_dir.mkdir(parents=True, exist_ok=True)

        target = target_dir / src.name
        shutil.move(str(src), target)
        return target
