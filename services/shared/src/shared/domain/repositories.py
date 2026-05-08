from abc import ABC, abstractmethod
from uuid import UUID
from .photo import Photo

class PhotoRepository(ABC):

    @abstractmethod
    async def register_photo(self, path: str) -> Photo:
        pass

    @abstractmethod
    async def register_photos(self, paths: list[str]) -> list[Photo]:
        pass

    @abstractmethod
    async def update_hashes(self, photo_id: UUID, phash: str, ahash: str, dhash: str):
        pass

    @abstractmethod
    async def update_tags(self, photo_id: UUID, tags: list[str]):
        pass
