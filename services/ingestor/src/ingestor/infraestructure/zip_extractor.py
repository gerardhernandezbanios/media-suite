# infraestructure/zip_extractor.py
import shutil
import zipfile
from pathlib import Path
from ingestor.config import Config

class ZipExtractor:
    def extract(self, zip_file: Path) -> list[Path]:
        tmp_dir = Config.SOURCE_DIR / f"tmp_zip_{zip_file.stem}"
        tmp_dir.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(zip_file, "r") as z:
            z.extractall(tmp_dir)

        return [p for p in tmp_dir.iterdir() if p.is_file()]

    def cleanup(self, zip_file: Path):
        tmp_dir = Config.SOURCE_DIR / f"tmp_zip_{zip_file.stem}"
        shutil.rmtree(tmp_dir)
        zip_file.unlink()
