# services/backend/app/media/infrastructure/ingestor/processor.py
from pathlib import Path
from datetime import datetime
import zipfile
import shutil


class IngestorProcessor:

    def process(self, temp_path: Path) -> list[Path]:
        """
        Devuelve una lista de rutas de archivos finales listos para procesar.
        Si es ZIP → extrae y devuelve los paths.
        Si es archivo normal → devuelve [temp_path].
        """
        if zipfile.is_zipfile(temp_path):
            return self._process_zip(temp_path)
        else:
            return [temp_path]

    def _process_zip(self, zip_path: Path) -> list[Path]:
        extract_dir = zip_path.parent / f"{zip_path.stem}_unzipped"
        extract_dir.mkdir(exist_ok=True)

        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(extract_dir)

        zip_path.unlink()  # borrar ZIP original

        # devolver solo archivos (no carpetas)
        return [p for p in extract_dir.rglob("*") if p.is_file()]
