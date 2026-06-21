# services/backend/app/filesystem/infrastructure/filesystem/job_filesystem_adapter.py
from services.backend.app.media.domain.services.job_port import JobPort

"""
# 🧩 1. Adaptador de filesystem para jobs: JobFilesystemAdapter

    Implementa JobPort:
        create_job(job_id, files):
            crea /work/incoming/{job_id}
            guarda ficheros
            escribe status.json
        get_pending_jobs():
            lista carpetas en /work/incoming
            lee status.json y devuelve Job agregados.
        update_status(job_id, status, error_message=None)
        move_job(job_id, from_state, to_state)
        
"""
import json
import shutil
from pathlib import Path
from typing import List
from datetime import datetime

from services.backend.app.media.domain.entities.job import Job
from services.backend.app.media.domain.value_objects.job_status import JobStatus
from services.backend.app.media.domain.services.job_port import JobPort


class JobFilesystemAdapter(JobPort):

    def __init__(self, base_path: str = "/work"):
        self.base = Path(base_path)
        self.incoming = self.base / "incoming"
        self.processing = self.base / "processing"
        self.done = self.base / "done"
        self.error = self.base / "error"

        for p in [self.incoming, self.processing, self.done, self.error]:
            p.mkdir(parents=True, exist_ok=True)

    def _job_folder(self, status: JobStatus, job_id: str) -> Path:
        return {
            JobStatus.PENDING: self.incoming,
            JobStatus.PROCESSING: self.processing,
            JobStatus.DONE: self.done,
            JobStatus.ERROR: self.error,
        }[status] / job_id

    def _status_file(self, folder: Path) -> Path:
        return folder / "status.json"

    def create_job(self, job: Job) -> None:
        folder = self._job_folder(JobStatus.PENDING, job.id)
        folder.mkdir(parents=True, exist_ok=True)
        self._write_status(folder, job)

    def get_job(self, job_id: str) -> Job:
        for status in JobStatus:
            folder = self._job_folder(status, job_id)
            if folder.exists():
                return self._read_status(folder)
        raise FileNotFoundError(f"Job {job_id} not found")

    def list_pending_jobs(self) -> List[Job]:
        jobs = []
        for folder in self.incoming.iterdir():
            if folder.is_dir():
                jobs.append(self._read_status(folder))
        return jobs

    def update_status(self, job_id: str, status: JobStatus, error_message=None) -> None:
        job = self.get_job(job_id)
        job.status = status
        job.updated_at = datetime.utcnow()
        job.error_message = error_message

        old_folder = self._job_folder(job.status, job_id)
        self._write_status(old_folder, job)

    def move_job_to(self, job_id: str, new_status: JobStatus) -> None:
        job = self.get_job(job_id)
        old_folder = self._job_folder(job.status, job_id)
        new_folder = self._job_folder(new_status, job_id)

        shutil.move(str(old_folder), str(new_folder))
        job.status = new_status
        self._write_status(new_folder, job)

    def _write_status(self, folder: Path, job: Job) -> None:
        status_file = self._status_file(folder)
        data = {
            "id": job.id,
            "status": job.status.value,
            "files": job.files,
            "created_at": job.created_at.isoformat(),
            "updated_at": job.updated_at.isoformat(),
            "error_message": job.error_message,
        }
        status_file.write_text(json.dumps(data, indent=2))

    def _read_status(self, folder: Path) -> Job:
        data = json.loads(self._status_file(folder).read_text())
        return Job(
            id=data["id"],
            status=JobStatus(data["status"]),
            files=data["files"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            error_message=data.get("error_message"),
        )
