import shutil
import zipfile
from pathlib import Path

from ingestor.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)


class ZipExtractor:
    def extract(self, zip_file: Path, source_dir: Path) -> list[Path]:
        logger.info(f"Extracting ZIP file: {zip_file}")
        tmp_dir = source_dir / f"tmp_zip_{zip_file.stem}"
        tmp_dir.mkdir(parents=True, exist_ok=True)

        # Asegura cierre correcto del ZIP
        with zipfile.ZipFile(zip_file, "r") as z:
            z.extractall(tmp_dir)

        return [p for p in tmp_dir.iterdir() if p.is_file()]

    def cleanup(self, zip_file: Path, source_dir: Path):
        tmp_dir = source_dir / f"tmp_zip_{zip_file.stem}"
        logger.info(f"Removing temporary directory: {tmp_dir} and ZIP file: {zip_file}")

        # Borrar carpeta temporal
        try:
            shutil.rmtree(tmp_dir)
        except FileNotFoundError:
            logger.warning(f"Temporary directory not found: {tmp_dir}")
        except Exception as e:
            logger.error(f"Error removing temporary directory {tmp_dir}: {e}")

        # Borrar ZIP original
        try:
            zip_file.unlink()
        except FileNotFoundError:
            logger.warning(f"ZIP file already removed: {zip_file}")
        except Exception as e:
            logger.error(f"Error removing ZIP file {zip_file}: {e}")
