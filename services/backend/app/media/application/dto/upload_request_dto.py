# services/backend/app/media/application/dto/upload_request_dto.py
from ast import List

from pydantic import BaseModel

class UploadRequestDTO(BaseModel):
    files: List[UploadFile]
