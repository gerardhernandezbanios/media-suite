from datetime import datetime

from PIL import Image
from PIL.ExifTags import TAGS


def get_exif_date(file):
    try:
        with Image.open(file) as img:
            exif = img._getexif()
            if exif:
                for tag, value in exif.items():
                    if TAGS.get(tag) == "DateTimeOriginal":
                        return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception:
        pass

    return datetime.fromtimestamp(file.stat().st_mtime)
