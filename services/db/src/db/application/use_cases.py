# applicaton/use_cases.py
from uuid import UUID
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from db.infrastructure.db.repositories import PhotoRepository

async def register_photo(path: str, session: AsyncSession):
    repo = PhotoRepository(session)
    existing = await repo.get_by_path(path)
    if existing:
        return existing
    photo = await repo.create_photo(path)
    await session.commit()
    return photo

async def update_photo_hashes(photo_id: UUID, phash: str | None, ahash: str | None, dhash: str | None, session: AsyncSession):
    repo = PhotoRepository(session)
    await repo.update_hashes(photo_id, phash, ahash, dhash)
    await session.commit()

async def update_photo_tags(photo_id: UUID, tags: List[str], session: AsyncSession):
    repo = PhotoRepository(session)
    await repo.replace_tags(photo_id, tags)
    await session.commit()

async def get_photo_by_id(photo_id: UUID, session: AsyncSession):
    repo = PhotoRepository(session)
    return await repo.get_by_id(photo_id)

async def get_photo_by_path(path: str, session: AsyncSession):
    repo = PhotoRepository(session)
    return await repo.get_by_path(path)
