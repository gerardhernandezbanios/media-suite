# infrastructure/file_system.py
import shutil
from datetime import datetime
from pathlib import Path

from ingestor.domain.exif_reader import get_exif_date


class FileSystem:
    def move(self, src: Path, dst: Path):
        shutil.move(str(src), str(dst))

    def now(self) -> datetime:
        return datetime.now()

    def get_date(self, file: Path) -> datetime:
        return get_exif_date(file)
