# services/backend/app/media/domain/entities/media_item.py
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from .value_objects import MediaType, MediaPath, Checksum

@dataclass
class MediaItem:
    id: Optional[int]
    type: MediaType
    original_path: str
    final_path: Optional[MediaPath]
    captured_at: datetime
    imported_at: datetime
    checksum: Optional[Checksum]
    width: Optional[int] = None
    height: Optional[int] = None
    duration_seconds: Optional[float] = None
    tags: List[str] = None

    def is_photo(self) -> bool:
        return self.type == MediaType.PHOTO

    def is_video(self) -> bool:
        return self.type == MediaType.VIDEO

