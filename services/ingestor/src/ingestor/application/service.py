# application/service.py
from pathlib import Path

from ingestor.config import Config
from ingestor.domain.classifier import classify
from ingestor.domain.mover import compute_destination, compute_unique_name
from ingestor.domain.stats import Stats
from ingestor.infrastructure.file_system import FileSystem
from ingestor.infrastructure.logging_base import IngestLogger
from ingestor.infrastructure.zip_extractor import ZipExtractor


class IngestService:
    def __init__(self, logger: IngestLogger):
        self.logger = logger
        self.fs = FileSystem()
        self.zip = ZipExtractor()

    def process_file(self, file: Path):
        file_type = classify(file)

        if file_type == "zip":
            return self._process_zip(file)

        if file_type == "unsupported":
            Stats.global_stats["unsupported"] += 1
            self.logger.log_unsupported(file)
            return

        root = {
            "image": Config.IMAGES_ROOT,
            "video": Config.VIDEOS_ROOT,
            "animation": Config.ANIMATIONS_ROOT,
        }[file_type]

        self._move_and_log(file, root)

    def _move_and_log(
        self, file: Path, root_dest: Path, special_folder=None, zip_origin=None
    ):
        dest_dir = compute_destination(file, root_dest, special_folder)
        dest_dir.mkdir(parents=True, exist_ok=True)
        date = self.fs.get_date(file)

        new_path = compute_unique_name(dest_dir, file)

        self.fs.move(file, new_path)
        self.logger.log_move(file, new_path, self.fs.now(), zip_origin)

        Stats.update_global(file, special_folder)
        if not special_folder:
            Stats.update_by_month(file, str(date.year), f"{date.month:02d}")

    def _process_zip(self, file: Path):
        extracted_files = self.zip.extract(file)

        for extracted in extracted_files:
            self.process_file(extracted)

        self.zip.cleanup(file)
