# services/backend/app/media/domain/entities/job.py

from dataclasses import dataclass   
from datetime import datetime
from typing import List, Optional

from services.backend.app.media.domain.value_objects.job_status import JobStatus

@dataclass
class Job:
    id: int
    status: JobStatus
    created_at: datetime
    updated_at: datetime
    files: List[str]
    error_message: Optional[str]
