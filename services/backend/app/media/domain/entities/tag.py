# services/backend/app/media/domain/entities/tag.py

from dataclasses import dataclass
from typing import Optional


@dataclass
class Tag:
    id: Optional[int]
    name: str
