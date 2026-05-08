# infrastructure/file_system.py
import shutil
from pathlib import Path

from ingestor.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)


class FileSystem:
    def move(self, src: Path, dst: Path):
        dst.parent.mkdir(parents=True, exist_ok=True)
        logger.info(f"Moving file from {src} to {dst}")
        shutil.move(str(src), str(dst))
