# services/backend/app/media/infrastructure/exif/extractor.py
from pathlib import Path
from datetime import datetime
from typing import Optional
from PIL import Image, ExifTags


class ExifData:
    def __init__(
        self,
        created_at: Optional[datetime],
        width: Optional[int],
        height: Optional[int],
        orientation: Optional[int],
        camera_model: Optional[str],
    ):
        self.created_at = created_at
        self.width = width
        self.height = height
        self.orientation = orientation
        self.camera_model = camera_model


class ExifExtractor:

    def extract(self, path: Path) -> ExifData:
        try:
            img = Image.open(path)
            exif = img._getexif()

            if not exif:
                return ExifData(None, img.width, img.height, None, None)

            # Convertir IDs numéricos a nombres
            exif_data = {
                ExifTags.TAGS.get(tag_id, tag_id): value
                for tag_id, value in exif.items()
            }

            # Fecha de captura
            date_str = exif_data.get("DateTimeOriginal") or exif_data.get("DateTime")
            created_at = (
                datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S")
                if date_str
                else None
            )

            return ExifData(
                created_at=created_at,
                width=img.width,
                height=img.height,
                orientation=exif_data.get("Orientation"),
                camera_model=exif_data.get("Model"),
            )

        except Exception:
            return ExifData(None, None, None, None, None)
