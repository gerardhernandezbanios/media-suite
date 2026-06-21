# services/backend/app/media/application/use_cases/upload_media_use_case.py
"""
# 🧩 1. Use case: UploadMediaUseCase
# Este es el caso de uso que llama la API.

# Responsabilidades:

# Recibir lista de ficheros subidos (FastAPI UploadFile o paths temporales).

# Detectar si cada fichero es:

# Imagen

# Vídeo

# ZIP

# Si es ZIP → descomprimir en un directorio temporal.

# Generar una lista plana de paths reales.

# Encolar cada fichero en la cola (QueuePort) para ingesta asíncrona.

# Devolver un job_id o lista de IDs.

# Este caso de uso NO procesa EXIF, ni hashing, ni mueve ficheros.
# Solo prepara y encola.
"""
from services.backend.app.media.application.dto.upload_result_dto import UploadResultDTO
from services.backend.app.media.application.dto.uploaded_file_dto import UploadedFileDTO
from services.backend.app.media.domain.services.queue_port import QueuePort
from services.backend.app.media.domain.services.temp_file_system_port import TempFileSystemPort
from services.backend.app.media.domain.services.zip_extractor_port import ZipExtractorPort


class UploadMediaUseCase:
    def __init__(
        self,
        temp_fs: TempFileSystemPort,
        zip_extractor: ZipExtractorPort,
        queue: QueuePort,
    ):
        self._temp_fs = temp_fs
        self._zip_extractor = zip_extractor
        self._queue = queue

    async def execute(self, files: list[UploadedFileDTO]) -> UploadResultDTO:
        temp_dir = await self._temp_fs.create_temp_dir()
        all_paths = []

        for dto in files:
            temp_path = await self._temp_fs.save_upload(dto, temp_dir)

            if dto.filename.lower().endswith(".zip"):
                extracted = await self._zip_extractor.extract(temp_path, temp_dir)
                all_paths.extend(extracted)
            else:
                all_paths.append(temp_path)

        job_ids = []
        for path in all_paths:
            job_id = await self._queue.enqueue("ingest", {"temp_path": path})
            job_ids.append(job_id)

        return UploadResultDTO(job_ids=job_ids)
