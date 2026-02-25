from dataclasses import dataclass
from uuid import UUID

@dataclass
class Photo:
    id: UUID
    path: str
