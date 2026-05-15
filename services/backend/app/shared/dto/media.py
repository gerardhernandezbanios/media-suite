from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class MediaTypeDTO(str, Enum):
    IMAGE = "image"
    VIDEO = "video"

class MediaMetadataDTO(BaseModel):
    width: int | None
    height: int | None
    orientation: int | None

    camera_make: str | None
    camera_model: str | None
    lens_model: str | None
    iso: int | None
    aperture: float | None
    shutter_speed: str | None
    focal_length: float | None
    created_at: datetime | None

    duration: float | None
    video_codec: str | None
    audio_codec: str | None
    frame_rate: float | None
    bit_rate: int | None


class MediaItemDTO(BaseModel):
    id: int
    type: MediaTypeDTO
    filename: str
    filepath: str
    sha256: str
    phash: str | None
    size_bytes: int
    width: int | None
    height: int | None
    duration: float | None
    created_at: datetime
    ingested_at: datetime
    metadata: MediaMetadataDTO | None

    class Config:
        from_attributes = True
