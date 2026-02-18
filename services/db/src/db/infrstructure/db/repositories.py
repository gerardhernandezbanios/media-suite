from typing import Optional, List
from uuid import UUID
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from .models import PhotoORM, PhotoHashesORM, PhotoTagORM
from .mappers import photo_orm_to_domain
from db.domain.models import Photo

class PhotoRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_photo(self, path: str) -> Photo:
        photo = PhotoORM(path=path)
        self.session.add(photo)
        await self.session.flush()
        await self.session.refresh(photo)
        return photo_orm_to_domain(photo)

    async def get_by_id(self, photo_id: UUID) -> Optional[Photo]:
        result = await self.session.execute(
            select(PhotoORM).where(PhotoORM.id == photo_id)
        )
        photo = result.scalar_one_or_none()
        return photo_orm_to_domain(photo) if photo else None

    async def get_by_path(self, path: str) -> Optional[Photo]:
        result = await self.session.execute(
            select(PhotoORM).where(PhotoORM.path == path)
        )
        photo = result.scalar_one_or_none()
        return photo_orm_to_domain(photo) if photo else None

    async def update_hashes(self, photo_id: UUID, phash: str | None, ahash: str | None, dhash: str | None) -> None:
        hashes = await self.session.get(PhotoHashesORM, photo_id)
        if hashes is None:
            hashes = PhotoHashesORM(photo_id=photo_id)
            self.session.add(hashes)
        hashes.phash = phash
        hashes.ahash = ahash
        hashes.dhash = dhash

    async def replace_tags(self, photo_id: UUID, tags: List[str]) -> None:
        await self.session.execute(
            delete(PhotoTagORM).where(PhotoTagORM.photo_id == photo_id)
        )
        self.session.add_all(
            [PhotoTagORM(photo_id=photo_id, tag=t) for t in tags]
        )
