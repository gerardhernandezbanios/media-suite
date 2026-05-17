#services/backend/app/media/domain/entities.py
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from enum import Enum

@dataclass
class MediaMetadata:
    id: Optional[int]
    media_id: int

    # Imagen
    width: Optional[int]
    height: Optional[int]
    orientation: Optional[int]

    # EXIF
    camera_make: Optional[str]
    camera_model: Optional[str]
    lens_model: Optional[str]
    iso: Optional[int]
    aperture: Optional[float]
    shutter_speed: Optional[str]
    focal_length: Optional[float]
    created_at: Optional[datetime]

    # Vídeo
    duration: Optional[float]
    video_codec: Optional[str]
    audio_codec: Optional[str]
    frame_rate: Optional[float]
    bit_rate: Optional[int]


class MediaType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

from app.media.domain.value_objects import MediaType
from app.media.domain.exif import ExifData


@dataclass
class MediaItem:
    id: Optional[int]
    type: MediaType
    filename: str
    filepath: str
    sha256: str
    phash: Optional[str]
    size_bytes: int
    width: Optional[int]
    height: Optional[int]
    duration: Optional[float]
    created_at: datetime
    ingested_at: datetime

    @staticmethod
    def create_from_raw(
        path: Path,
        exif: Optional[ExifData],
        sha256: str,
        phash: Optional[str],
        now: datetime,
    ) -> "MediaItem":
        stat = path.stat()
        size_bytes = stat.st_size

        # tipo muy simple: imagen vs vídeo (puedes refinarlo)
        suffix = path.suffix.lower()
        if suffix in {".jpg", ".jpeg", ".png", ".gif", ".webp"}:
            media_type = MediaType.IMAGE
        elif suffix in {".mp4", ".mov", ".mkv", ".avi"}:
            media_type = MediaType.VIDEO
        else:
            media_type = MediaType.UNKNOWN

        width = exif.width if exif else None
        height = exif.height if exif else None
        duration = exif.duration if exif else None

        created_at = (
            exif.created_at
            if exif and exif.created_at is not None
            else datetime.fromtimestamp(stat.st_mtime)
        )

        return MediaItem(
            id=None,
            type=media_type,
            filename=path.name,
            filepath=str(path),  # se actualizará tras mover a la librería
            sha256=sha256,
            phash=phash,
            size_bytes=size_bytes,
            width=width,
            height=height,
            duration=duration,
            created_at=created_at,
            ingested_at=now,
        )


# @dataclass
# class MediaItem:
#     id: Optional[int]
#     type: MediaType
#     filename: str
#     filepath: str
#     sha256: str
#     phash: Optional[str]
#     size_bytes: int
#     width: Optional[int]
#     height: Optional[int]
#     duration: Optional[float]
#     created_at: datetime
#     ingested_at: datetime




@dataclass
class Album:
    id: Optional[int]
    name: str
    created_at: datetime


@dataclass
class Tag:
    id: Optional[int]
    name: str
