# services/backend/app/media/domain/exif.py
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class ExifData:
    width: Optional[int] = None
    height: Optional[int] = None
    orientation: Optional[int] = None

    camera_make: Optional[str] = None
    camera_model: Optional[str] = None
    lens_model: Optional[str] = None
    iso: Optional[int] = None
    aperture: Optional[float] = None
    shutter_speed: Optional[str] = None
    focal_length: Optional[float] = None
    created_at: Optional[datetime] = None

    duration: Optional[float] = None
    video_codec: Optional[str] = None
    audio_codec: Optional[str] = None
    frame_rate: Optional[float] = None
    bit_rate: Optional[int] = None
