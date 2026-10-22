# services/backend/app/media/domain/value_objects/media_metadata.py

from dataclasses import dataclass
import datetime
from typing import Optional


@dataclass(frozen=True)
class MediaMetadata:
    width: Optional[int]
    height: Optional[int]
    duration_seconds: Optional[float]
    camera_make: Optional[str]
    camera_model: Optional[str]
    lens_model: Optional[str]
    iso: Optional[int]
    aperture: Optional[float]
    shutter_speed: Optional[str]
    focal_length: Optional[float]
    created_at: Optional[datetime]
    video_codec: Optional[str]
    audio_codec: Optional[str]
    frame_rate: Optional[float]
    bit_rate: Optional[int]
