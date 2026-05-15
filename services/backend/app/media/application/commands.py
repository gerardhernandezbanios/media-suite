# services/backend/app/media/application/commands.py
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from fastapi import UploadFile

from app.media.infrastructure.filesystem.storage import FilesystemStorage
from app.media.infrastructure.ingestor.processor import IngestorProcessor
from app.media.infrastructure.hashing.sha256 import compute_sha256
from app.media.infrastructure.hashing.perceptual import compute_phash
from app.media.infrastructure.db.repositories import MediaRepository
from app.media.infrastructure.db.models import MediaItemModel
from app.media.domain.entities import MediaType


@dataclass
class UploadMediaCommand:
    file: UploadFile


class UploadMediaService:

    def __init__(self, repo: MediaRepository):
        self.repo = repo
        self.storage = FilesystemStorage()
        self.ingestor = IngestorProcessor()

    async def execute(self, cmd: UploadMediaCommand):
        # 1. Guardar temporalmente
        temp_path = self.storage.save_temp(cmd.file, cmd.file.filename)

        # 2. Ingestor (zip o archivo normal)
        paths = self.ingestor.process(temp_path)

        saved_items = []

        for path in paths:
            # 3. Determinar tipo
            media_type = self._detect_type(path)

            # 4. Extraer fecha de creación
            created_at = self._extract_created_at(path)

            # 5. Mover a ubicación final
            final_path = self.storage.move_to_final_location(
                path, media_type.value, created_at
            )

            # 6. Hashes
            sha256 = compute_sha256(final_path)
            phash = compute_phash(final_path) if media_type == MediaType.IMAGE else None

            # 7. Crear modelo DB
            model = MediaItemModel(
                type=media_type,
                filename=final_path.name,
                filepath=str(final_path),
                sha256=sha256,
                phash=phash,
                size_bytes=final_path.stat().st_size,
                width=None,
                height=None,
                duration=None,
                created_at=created_at,
                ingested_at=datetime.utcnow(),
            )

            await self.repo.add(model)
            saved_items.append(model)

        return saved_items

    def _detect_type(self, path: Path) -> MediaType:
        ext = path.suffix.lower()
        if ext in [".jpg", ".jpeg", ".png", ".webp"]:
            return MediaType.IMAGE
        return MediaType.VIDEO

    def _extract_created_at(self, path: Path) -> datetime:
        # TODO: leer EXIF si es imagen
        ts = path.stat().st_mtime
        return datetime.fromtimestamp(ts)
