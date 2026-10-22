# services/backend/app/media/application/dto/upload_result_dto.py
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class UploadResultDTO:
    job_ids: List[str]
