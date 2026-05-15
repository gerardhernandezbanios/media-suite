from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class MediaTypeDTO(str, Enum):
    IMAGE = "image"
    VIDEO = "video"


class MediaItemDTO(BaseModel):
    id: int
    type: MediaTypeDTO
    filename: str
    filepath: str
    sha256: str
    phash: str | None
    size_bytes: int
    width: int | None
    height: int | None
    duration: float | None
    created_at: datetime
    ingested_at: datetime

    class Config:
        from_attributes = True
