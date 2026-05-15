#services/backend/app/media/api/media.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.media.infrastructure.db.repositories import MediaRepository
from app.media.api.mappers import domain_to_dto

router = APIRouter()


@router.get("/")
async def list_media(session: AsyncSession = Depends(get_session)):
    repo = MediaRepository(session)
    items = await repo.list()
    return [domain_to_dto(item) for item in items]
