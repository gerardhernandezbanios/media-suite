# services/backend/app/media/application/dto/media_item_dto.py

from dataclasses import dataclass
import datetime
from typing import List, Optional
from pydantic import BaseModel

class MediaItemDTO(BaseModel):
    id: int
    type: str
    final_path: str
    captured_at: datetime
    imported_at: datetime
    width: Optional[int]
    height: Optional[int]
    duration_seconds: Optional[float]
    tags: List[str]
