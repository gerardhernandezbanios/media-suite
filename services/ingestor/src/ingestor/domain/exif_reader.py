# domain\exif_reader.py
from datetime import datetime
from pathlib import Path
from PIL import Image, ExifTags

def get_exif_date(file: Path) -> datetime:
    try:
        with Image.open(file) as img:
            exif = img._getexif()
            if exif:
                for tag, value in exif.items():
                    if ExifTags.TAGS.get(tag) == "DateTimeOriginal":
                        return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception:
        pass

    return datetime.fromtimestamp(file.stat().st_mtime)
