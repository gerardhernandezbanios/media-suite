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


@dataclass
class Album:
    id: Optional[int]
    name: str
    created_at: datetime


@dataclass
class Tag:
    id: Optional[int]
    name: str
