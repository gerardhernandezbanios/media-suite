# ingestor/application/service.py
from pathlib import Path

from ingestor.domain.mover import compute_destination, compute_unique_name
from ingestor.infrastructure.logging.logger import get_logger

_logger = get_logger(__name__)

class IngestService:
    def __init__(self, logger, inspector, classifier, renamer, fs, zip_extractor, config,
    ):
        self.logger = logger
        self.inspector = inspector
        self.classifier = classifier
        self.renamer = renamer
        self.fs = fs
        self.zip = zip_extractor
        self.config = config

        self.CATEGORY_ROOTS = {
            "images": config.IMAGES_ROOT,
            "videos": config.VIDEOS_ROOT,
            "animations": config.ANIMATIONS_ROOT,
            "archives": config.UNSUPPORTED_ROOT,
            "unsupported": config.UNSUPPORTED_ROOT,
        }

    def process_file(self, path: Path):
        _logger.info(f"Processing file: {path}")

        info = self.inspector.inspect(path)

        if info.is_directory:
            return

        if info.is_archive:
            extracted = self.zip.extract(path, self.config.SOURCE_DIR)
            for f in extracted:
                self.process_file(f)
            return

        normalized = self.renamer.normalize(path)
        if normalized != path:
            path.rename(normalized)
            path = normalized

        category = self.classifier.classify(info)
        root = self._select_root(category)

        dest_dir = compute_destination(path, root)
        final_path = compute_unique_name(dest_dir, path)

        self.fs.move(path, final_path)
        if category == "unsupported":
            self.logger.log_unsupported(path)
        else:
            self.logger.log_move(path, final_path, info.mime, category)

        if info.is_archive:
            self.zip.cleanup(path, self.config.SOURCE_DIR)

    def _select_root(self, category: str) -> Path:
        return self.CATEGORY_ROOTS.get(category, self.config.UNSUPPORTED_ROOT)
