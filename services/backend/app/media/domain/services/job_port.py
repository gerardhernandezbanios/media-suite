# services/backend/app/media/domain/entities/job_status.py

"""
Responsabilidades:

    Crear un job en /work/incoming/{job_id}
    Escribir/leer status.json
    Mover la carpeta entre incoming → processing → done/error
    Listar jobs pendientes (incoming)

"""
from abc import ABC, abstractmethod
from typing import List
from .job import Job
from .job_status import JobStatus

class JobPort(ABC):

    @abstractmethod
    def create_job(self, job: Job) -> None:
        ...

    @abstractmethod
    def get_job(self, job_id: str) -> Job:
        ...

    @abstractmethod
    def list_pending_jobs(self) -> List[Job]:
        ...

    @abstractmethod
    def update_status(self, job_id: str, status: JobStatus, error_message: str | None = None) -> None:
        ...

    @abstractmethod
    def move_job_to(self, job_id: str, new_status: JobStatus) -> None:
        ...
