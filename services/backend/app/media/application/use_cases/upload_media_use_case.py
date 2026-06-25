# services/backend/app/media/application/use_cases/upload_media_use_case.py
"""
# 🧩 1. Use case: UploadMediaUseCase

        Responsabilidad principal:

            Recibir la petición de subida (1 fichero, varios, ZIP).
            Crear un job:
                Generar job_id
                Crear carpeta /work/incoming/{job_id}
                Guardar todos los ficheros tal cual:
                    Foto1.jpg
                    Video1.mp4
                    Archivo.zip
                Crear status.json con:
                    Status = "pending"
                    Lista de ficheros
                    Timestamps  
                Devolver job_id al controlador.

    Este caso de uso no procesa nada, solo crea el job. 
    Eso mantiene el sistema asíncrono y limpio.
"""
import uuid
from typing import List
from fastapi import UploadFile

from media.domain.entities.job import Job
from media.domain.value_objects.job_status import JobStatus
from media.domain.services.job_port import JobPort


class UploadMediaUseCase:

    def __init__(self, job_port: JobPort):
        self.job_port = job_port

    async def execute(self, files: List[UploadFile]) -> str:
        job_id = str(uuid.uuid4())

        job = Job(
            id=job_id,
            status=JobStatus.PENDING,
            files=[f.filename for f in files],
        )

        # Crear job en filesystem
        self.job_port.create_job(job)

        # Guardar ficheros dentro del job
        job_folder = self.job_port._job_folder(JobStatus.PENDING, job_id)

        for file in files:
            dest = job_folder / file.filename
            with dest.open("wb") as f:
                f.write(await file.read())

        return job_id
