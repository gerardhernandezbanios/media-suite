# services/backend/app/media/application/dto/job_status_dto.py
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class JobStatusDTO(BaseModel):
    id: str
    status: str
    error_message: Optional[str]
    files: List[str]
    created_at: datetime
    updated_at: datetime
