# domain/models.py
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from typing import List, Optional

@dataclass
class Photo:
    id: UUID
    path: str
    created_at: datetime
    updated_at: datetime
    tags: List[str]
    phash: Optional[str] = None
    ahash: Optional[str] = None
    dhash: Optional[str] = None
