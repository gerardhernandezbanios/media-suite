# services/backend/app/media/domain/services/media_path_factory.py
from datetime import datetime
from .value_objects import MediaType, MediaPath

class MediaPathFactory:
    def __init__(self, root: str):
        self._root = root

    def build(self, media_type: MediaType, captured_at: datetime, filename: str) -> MediaPath:
        type_dir = "photos" if media_type == MediaType.PHOTO else "videos"
        return MediaPath(
            root=self._root,
            type_dir=type_dir,
            year=captured_at.year,
            month=captured_at.month,
            filename=filename,
        )
