# infrastructure/zip_extractor.py
import shutil
import zipfile
from pathlib import Path

from ingestor.config import Config
from ingestor.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)


class ZipExtractor:
    def extract(self, zip_file: Path) -> list[Path]:
        logger.info(f"Extracting ZIP file: {zip_file}")
        tmp_dir = Config.SOURCE_DIR / f"tmp_zip_{zip_file.stem}"
        tmp_dir.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(zip_file, "r") as z:
            z.extractall(tmp_dir)

        return [p for p in tmp_dir.iterdir() if p.is_file()]

    def cleanup(self, zip_file: Path):
        tmp_dir = Config.SOURCE_DIR / f"tmp_zip_{zip_file.stem}"
        logger.info(f"Removing temporary directory: {tmp_dir} and ZIP file: {zip_file}")
        shutil.rmtree(tmp_dir)
        zip_file.unlink()
