from pathlib import Path

from ingestor.config import Config
from ingestor.domain.classifier import Classifier
from ingestor.domain.file_inspector import FileInspector
from ingestor.domain.mover import compute_destination, compute_unique_name
from ingestor.domain.renamer import Renamer
from ingestor.infrastructure.file_system import FileSystem
from ingestor.infrastructure.zip_extractor import ZipExtractor


class IngestService:
    def __init__(self, logger):
        self.logger = logger
        self.inspector = FileInspector()
        self.classifier = Classifier()
        self.renamer = Renamer()
        self.fs = FileSystem()
        self.zip = ZipExtractor()

    def process_file(self, path: Path):
        info = self.inspector.inspect(path)

        # 1. Directorios no se procesan
        if info.is_directory:
            return

        # 2. ZIP → extraer y reinyectar
        if info.is_archive:
            extracted = self.zip.extract(path, Config.SOURCE_DIR)
            for f in extracted:
                self.process_file(f)
            return

        # 3. Normalizar nombre
        normalized = self.renamer.normalize(path)
        if normalized != path:
            path.rename(normalized)
            path = normalized

        # 4. Clasificación
        category = self.classifier.classify(info)

        # 5. Seleccionar raíz según categoría
        root = self._select_root(category)

        # 6. Calcular destino final (root/YYYY/MM)
        dest_dir = compute_destination(path, root, category)

        # 7. Evitar colisiones
        final_path = compute_unique_name(dest_dir, path)

        # 8. Mover archivo
        self.fs.move(path, final_path)

        # 9. Registrar
        self.logger.log_ingest(path, final_path, category)

    CATEGORY_ROOTS = {
        "images": Config.IMAGES_ROOT,
        "videos": Config.VIDEOS_ROOT,
        "animations": Config.ANIMATIONS_ROOT,
        "archives": Config.UNSUPPORTED_ROOT,
        "unsupported": Config.UNSUPPORTED_ROOT,
    }

    def _select_root(self, category: str) -> Path:
        return self.CATEGORY_ROOTS.get(category, Config.UNSUPPORTED_ROOT)
