# ingestor/application/service.py
from pathlib import Path

from ingestor.domain.mover import compute_destination, compute_unique_name
from ingestor.infrastructure.logging.logger import get_logger

_logger = get_logger(__name__)

class IngestService:
    def __init__(
        self,
        logger,
        inspector,
        classifier,
        renamer,
        fs,
        zip_extractor,
        config
    ):
        self.logger = logger
        self.inspector = inspector
        self.classifier = classifier
        self.renamer = renamer
        self.fs = fs
        self.zip = zip_extractor
        self.config = config

        # Buffer interno para registrar al final
        self._pending_registrations: list[str] = []

        self.CATEGORY_ROOTS = {
            "images": config.IMAGES_ROOT,
            "videos": config.VIDEOS_ROOT,
            "animations": config.ANIMATIONS_ROOT,
            "archives": config.UNSUPPORTED_ROOT,
            "unsupported": config.UNSUPPORTED_ROOT,
        }

    async def process_file(self, path: Path, *, is_root=True):
        """Procesa un archivo o directorio. Si es root, registra al final."""
        _logger.info(f"Processing file: {path}")

        info = self.inspector.inspect(path)

        if info.is_directory:
            return

        if info.is_archive:
            try:
                await self._process_archive(path)
            except Exception as e:
                self.logger.log_unsupported(path)
                _logger.error(f"Error processing archive {path}: {e}")
                return

            path.unlink()

            # Si es root, registramos ahora
            if is_root:
                await self.flush_registrations()
            return

        # Normalización
        normalized = self.renamer.normalize(path)
        if normalized != path:
            path.rename(normalized)
            path = normalized

        # Clasificación
        category = self.classifier.classify(info)
        root = self._select_root(category)

        # Destino final
        dest_dir = compute_destination(path, root)
        final_path = compute_unique_name(dest_dir, path)

        # Movimiento
        self.fs.move(path, final_path)

        if category == "unsupported":
            self.logger.log_unsupported(path)
        else:
            self.logger.log_move(path, final_path, info.mime, category)
            self._pending_registrations.append(str(final_path))

        # Si es root, registramos ahora
        if is_root:
            await self.flush_registrations()

    async def _process_archive(self, path: Path):
        """Procesa un ZIP sin registrar todavía (lo hará el caller root)."""
        with self.zip.extract(path) as extracted:
            for f in extracted:
                await self.process_file(f, is_root=False)

    def _select_root(self, category: str) -> Path:
        return self.CATEGORY_ROOTS.get(category, self.config.UNSUPPORTED_ROOT)

    async def flush_registrations(self):
        """Registra todas las fotos procesadas en el servicio DB."""
        if not self._pending_registrations:
            return

        # try:
        #     await self.photo_repo.register_photos(self._pending_registrations)
        #     _logger.info(f"Registered {len(self._pending_registrations)} photos in DB")
        # except Exception as e:
        #     _logger.error(f"Error registering photos: {e}")

        self._pending_registrations.clear()
