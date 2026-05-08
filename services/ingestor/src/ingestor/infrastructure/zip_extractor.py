# ingestor/infrastructure/zip_extractor.py
import shutil
import tempfile
import zipfile
from contextlib import contextmanager
from pathlib import Path


class ZipExtractor:
    def __init__(self, work_dir: Path | None = None):
        self.work_dir = work_dir or Path(tempfile.gettempdir()) / "ingestor"

    @contextmanager
    def extract(self, zip_path: Path):
        self.work_dir.mkdir(parents=True, exist_ok=True)
        temp_dir = Path(tempfile.mkdtemp(dir=self.work_dir))

        try:
            with zipfile.ZipFile(zip_path, "r") as z:
                z.extractall(temp_dir)

            extracted_files = list(temp_dir.rglob("*"))
            yield extracted_files

        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)
