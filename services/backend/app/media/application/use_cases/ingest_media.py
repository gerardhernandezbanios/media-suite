# services/backend/app/media/application/use_cases/ingest_media.py
from datetime import datetime

from services.backend.app.media.domain.repositories.media_repository import MediaRepository
from services.backend.app.media.domain.services.file_system_port import FileSystemPort

from services.backend.app.media.domain.services.exif_reader import ExifReader
from services.backend.app.media.domain.services.hasher import Hasher
from services.backend.app.media.domain.services.media_path_factory import MediaPathFactory
from services.backend.app.media.domain.value_objects.media_type import MediaType  

class IngestMediaUseCase:
    def __init__(
        self,
        media_repo: MediaRepository,
        fs: FileSystemPort,
        exif_reader: ExifReader,
        hasher: Hasher,
        path_factory: MediaPathFactory,
    ):
        self._media_repo = media_repo
        self._fs = fs
        self._exif_reader = exif_reader
        self._hasher = hasher
        self._path_factory = path_factory

    async def execute(self, src_path: str, media_type: MediaType) -> MediaItem:
        exif = await self._exif_reader.read(src_path)
        checksum = await self._hasher.compute(src_path)

        captured_at = exif.captured_at or datetime.now()
        filename = src_path.split("/")[-1]
        dest_path = self._path_factory.build(media_type, captured_at, filename)

        await self._fs.move(src_path, dest_path)

        item = MediaItem(
            id=None,
            type=media_type,
            original_path=src_path,
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
