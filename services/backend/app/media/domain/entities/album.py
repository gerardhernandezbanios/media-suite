# services/backend/app/media/domain/entities/album.py
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class Album:
    id: Optional[int]
    name: str
    description: Optional[str]
    created_at: datetime
    media_ids: List[int]
