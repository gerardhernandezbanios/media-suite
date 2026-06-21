# services/backend/app/media/application/use_cases/ingest_single_media_use_case.py

"""
🧩 2. Use case: IngestSingleMediaUseCase
        Este es el caso de uso que ejecuta el worker.

        Responsabilidades:

            Leer EXIF
            Calcular hash
            Determinar tipo (foto/vídeo)
            Crear MediaPath final
            Mover fichero
            Persistir MediaItem
            Detectar duplicados (opcional)
            Devolver el MediaItem final

        Este caso de uso NO sabe nada de ZIPs ni de uploads.
"""

from datetime import datetime
import os

from services.backend.app.media.domain.entities.entities import MediaItem
from services.backend.app.media.domain.repositories.media_repository import MediaRepository
from services.backend.app.media.domain.services.exif_reader import ExifReader
from services.backend.app.media.domain.services.file_system_port import FileSystemPort
from services.backend.app.media.domain.services.hasher import Hasher
from services.backend.app.media.domain.services.media_path_factory import MediaPathFactory
from services.backend.app.media.domain.services.media_type_detector import MediaTypeDetector


class IngestSingleMediaUseCase:
    def __init__(
        self,
        media_repo: MediaRepository,
        fs: FileSystemPort,
        exif_reader: ExifReader,
        hasher: Hasher,
        path_factory: MediaPathFactory,
        type_detector: MediaTypeDetector,
    ):
        self._media_repo = media_repo
        self._fs = fs
        self._exif_reader = exif_reader
        self._hasher = hasher
        self._path_factory = path_factory
        self._type_detector = type_detector

    async def execute(self, temp_path: str) -> MediaItem:
        filename = os.path.basename(temp_path)

        media_type = self._type_detector.detect(filename)
        exif = await self._exif_reader.read(temp_path)
        checksum = await self._hasher.compute(temp_path)

        captured_at = exif.captured_at or datetime.now()
        dest_path = self._path_factory.build(media_type, captured_at, filename)

        await self._fs.move(temp_path, dest_path)

        item = MediaItem(
            id=None,
            type=media_type,
            original_path=temp_path,
            final_path=dest_path,
            captured_at=captured_at,
            imported_at=datetime.now(),
            checksum=checksum,
            width=exif.width,
            height=exif.height,
            duration_seconds=exif.duration_seconds,
            tags=[],
        )

        return await self._media_repo.save(item)
