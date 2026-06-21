from abc import ABC, abstractmethod
from typing import Optional, List
from datetime import datetime
from .entities import MediaItem

class MediaRepository(ABC):
    @abstractmethod
    async def save(self, item: MediaItem) -> MediaItem:
        ...

    @abstractmethod
    async def find_by_id(self, id_: int) -> Optional[MediaItem]:
        ...

    @abstractmethod
    async def find_by_checksum(self, checksum: str) -> List[MediaItem]:
        ...

    @abstractmethod
    async def list_by_date_range(self, start: datetime, end: datetime) -> List[MediaItem]:
        ...
