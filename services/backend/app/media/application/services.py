# services/backend/app/media/application/services.py
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import List

from fastapi import UploadFile

from app.media.domain.entities import MediaItem
from app.media.domain.repositories import MediaItemRepository
from app.media.domain.services import ExifReader, HashCalculator, MediaStorage
from app.media.domain.exif import ExifData
from app.media.application.commands import IngestMediaCommand
from app.shared.dto.media import MediaItemDTO
from app.media.infrastructure.db.mappers import domain_to_dto


class FileUploadService:
    def __init__(self, tmp_dir: Path):
        self.tmp_dir = tmp_dir

    async def save_and_expand(self, files: List[UploadFile]) -> List[Path]:
        from zipfile import ZipFile
        import shutil

        final_paths: List[Path] = []

        for file in files:
            tmp_path = await self._save_temp(file)

            if file.filename.lower().endswith(".zip"):
                with ZipFile(tmp_path, "r") as z:
                    for name in z.namelist():
                        if name.endswith("/"):
                            continue
                        target = self.tmp_dir / name
                        target.parent.mkdir(parents=True, exist_ok=True)
                        with z.open(name) as src, target.open("wb") as dst:
                            shutil.copyfileobj(src, dst)
                        final_paths.append(target)
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


class IngestMediaHandler:
    def __init__(
        self,
        exif_reader: ExifReader,
        hash_calculator: HashCalculator,
        storage: MediaStorage,
        repo: MediaItemRepository,
    ):
        self.exif_reader = exif_reader
        self.hash_calculator = hash_calculator
        self.storage = storage
        self.repo = repo

    async def handle(self, cmd: IngestMediaCommand) -> List[MediaItem]:
        results: List[MediaItem] = []
        now = datetime.utcnow()

        for path in cmd.paths:
            exif: ExifData | None = self.exif_reader.extract(path)
            sha = self.hash_calculator.sha256(path)
            ph = self.hash_calculator.phash(path)

            entity = MediaItem.create_from_raw(
                path=path,
                exif=exif,
                sha256=sha,
                phash=ph,
                now=now,
            )

            final_path = self.storage.move_to_library(path, entity)
            entity.filepath = str(final_path)

            saved = await self.repo.save(entity)
            results.append(saved)

        return results


class UploadMediaService:
    def __init__(
        self,
        uploader: FileUploadService,
        ingestor: IngestMediaHandler,
    ):
        self.uploader = uploader
        self.ingestor = ingestor

    async def handle(self, files: List[UploadFile]) -> List[MediaItemDTO]:
        paths = await self.uploader.save_and_expand(files)
        cmd = IngestMediaCommand(paths=paths)
        items = await self.ingestor.handle(cmd)
        return [domain_to_dto(item) for item in items]
