# services/backend/app/media/infrastructure/exif/extractor.py
from __future__ import annotations

from pathlib import Path
from typing import Optional

from PIL import Image, ExifTags

from app.media.domain.exif import ExifData
from app.media.domain.services import ExifReader


class PillowExifReader(ExifReader):
    def extract(self, path: Path) -> Optional[ExifData]:
        try:
            with Image.open(path) as img:
                exif_raw = img._getexif() or {}
                exif = {
                    ExifTags.TAGS.get(k, k): v
                    for k, v in exif_raw.items()
                }

                width, height = img.size

                created_at = None
                dt = exif.get("DateTimeOriginal") or exif.get("DateTime")
                if dt:
                    # simplificado; puedes parsear bien con datetime.strptime
                    from datetime import datetime

                    try:
                        created_at = datetime.strptime(dt, "%Y:%m:%d %H:%M:%S")
                    except Exception:
                        created_at = None

                return ExifData(
                    width=width,
                    height=height,
                    orientation=exif.get("Orientation"),
                    camera_make=exif.get("Make"),
                    camera_model=exif.get("Model"),
                    lens_model=exif.get("LensModel"),
                    iso=exif.get("ISOSpeedRatings"),
                    aperture=None,
                    shutter_speed=None,
                    focal_length=None,
                    created_at=created_at,
                )
        except Exception:
            return None
