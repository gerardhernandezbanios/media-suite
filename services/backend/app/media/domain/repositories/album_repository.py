# services/backend/app/media/domain/repositories/album_repository.py
from abc import ABC, abstractmethod
from typing import Optional, List
from .entities import Album

class AlbumRepository(ABC):
    @abstractmethod
    async def save(self, album: Album) -> Album:
        ...

    @abstractmethod
    async def find_by_id(self, id_: int) -> Optional[Album]:
        ...

    @abstractmethod
    async def list_all(self) -> List[Album]:
        ...
