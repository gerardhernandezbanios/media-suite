# services/backend/app/media/infrastructure/exif/exif_reader_adapter.py

from datetime import datetime
from pathlib import Path
from PIL import Image
from media.domain.services.exif_reader import ExifReaderPort
from media.domain.entities.exif import ExifData

class ExifReaderAdapter(ExifReaderPort):

    def read(self, file: Path) -> ExifData:
        """Lee EXIF. Si falla, usa fecha de modificación."""
        try:
            img = Image.open(file)
            exif = img.getexif()

            date_str = exif.get(36867)  # DateTimeOriginal
            if date_str:
                dt = datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S")
                return ExifData(captured_at=dt)

        except Exception:
            pass

        # fallback
        return ExifData(
            captured_at=datetime.fromtimestamp(file.stat().st_mtime)
        )
