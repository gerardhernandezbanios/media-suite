# services/backend/app/media/infrastructure/filesystem/media_path_factory_adapter.py

from pathlib import Path
from media.domain.services.media_path_factory import MediaPathFactoryPort
from media.domain.value_objects.media_type import MediaType

BASE_MEDIA = Path("/media")

class MediaPathFactoryAdapter(MediaPathFactoryPort):

    def build_path(self, file, media_type, exif, checksum) -> Path:
        year = exif.captured_at.year
        month = f"{exif.captured_at.month:02d}"

        folder = "photos" if media_type == MediaType.PHOTO else "videos"

        filename = f"{checksum}{file.suffix.lower()}"

        return BASE_MEDIA / folder / str(year) / month / filename
