# services/backend/app/media/domain/entities/job.py

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from services.backend.app.media.domain.value_objects.job_status import JobStatus

@dataclass
class Job:
    id: str
    status: JobStatus
    files: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    error_message: Optional[str] = None
