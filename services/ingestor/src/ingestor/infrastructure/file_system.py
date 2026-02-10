# infrastructure/file_system.py
import shutil
from datetime import datetime
from pathlib import Path

from ingestor.domain.exif_reader import get_exif_date
from ingestor.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)


class FileSystem:
    def move(self, src: Path, dst: Path):
        logger.info(f"Moving file from {src} to {dst}")
        shutil.move(str(src), str(dst))

    def now(self) -> datetime:
        return datetime.now()

    def get_date(self, file: Path) -> datetime:
        return get_exif_date(file)
