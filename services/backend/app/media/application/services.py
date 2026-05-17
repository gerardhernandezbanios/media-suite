# services/backend/app/media/application/services.py
from pathlib import Path
from zipfile import ZipFile
import shutil
from fastapi import UploadFile

from typing import List
from app.media.infrastructure.ingestor.processor import IngestorService
from app.shared.dto.media import MediaItemDTO
from app.media.application.services import FileUploadService
from app.media.infrastructure.db.mappers import domain_to_dto

class UploadMediaService:
    """
    Orquestador del proceso de subida:
    - Guarda y expande archivos
    - Llama al ingestor
    - Devuelve DTOs
    """

    def __init__(self, uploader: FileUploadService, ingestor: IngestorService):
        self.uploader = uploader
        self.ingestor = ingestor

    async def handle(self, files: list[UploadFile]) -> List[MediaItemDTO]:
        paths = await self.uploader.save_and_expand(files)
        items = await self.ingestor.ingest_many(paths)
        return [domain_to_dto(item) for item in items]


class FileUploadService:
    """
    Servicio de aplicación encargado de:
    - Guardar archivos temporales
    - Detectar ZIPs
    - Extraer ZIPs recursivamente
    - Devolver una lista plana de paths
    """

    def __init__(self, tmp_dir: Path):
        self.tmp_dir = tmp_dir

    async def save_and_expand(self, files: list[UploadFile]) -> list[Path]:
        final_paths: list[Path] = []

        for file in files:
            tmp_path = await self._save_temp(file)

            if file.filename.lower().endswith(".zip"):
                extracted = self._extract_zip(tmp_path)
                final_paths.extend(extracted)
            else:
                final_paths.append(tmp_path)

        return final_paths

    async def _save_temp(self, file: UploadFile) -> Path:
        target = self.tmp_dir / file.filename
        target.parent.mkdir(parents=True, exist_ok=True)

        with target.open("wb") as f:
            while chunk := await file.read(1024 * 1024):
                f.write(chunk)

        return target

    def _extract_zip(self, zip_path: Path) -> list[Path]:
        extracted: list[Path] = []

        with ZipFile(zip_path, "r") as z:
            for name in z.namelist():
                if name.endswith("/"):
                    continue

                target = self.tmp_dir / name
                target.parent.mkdir(parents=True, exist_ok=True)

                with z.open(name) as src, target.open("wb") as dst:
                    shutil.copyfileobj(src, dst)

                extracted.append(target)

        return extracted
