# services/backend/app/media/domain/value_objects/job_status.py

from enum import Enum
from dataclasses import dataclass

class JobStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    DONE = "done"
    FAILED = "failed"

