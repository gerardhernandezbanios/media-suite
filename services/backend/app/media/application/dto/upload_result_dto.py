# services/backend/app/media/application/dto/upload_result_dto.py
from dataclasses import dataclass


@dataclass
class UploadResultDTO:
    job_ids: list[str]
