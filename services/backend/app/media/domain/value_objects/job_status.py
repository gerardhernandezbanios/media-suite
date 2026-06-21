# services/backend/app/media/domain/value_objects/job_status.py

from enum import Enum
from dataclasses import dataclass

class JobStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    FAILED = "failed"
    DONE = "done"

