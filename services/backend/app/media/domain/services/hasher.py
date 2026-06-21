# services/backend/app/media/domain/services/hasher.py
from abc import ABC, abstractmethod
from .value_objects import Checksum

class Hasher(ABC):
    @abstractmethod
    async def compute(self, path: str) -> Checksum:
        ...
