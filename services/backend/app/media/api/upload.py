#services/backend/app/media/api/upload.py
from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.media.application.commands import UploadMediaCommand, UploadMediaService
from app.media.infrastructure.db.repositories import MediaRepository
from app.core.db import get_session  # lo creamos ahora

router = APIRouter()


@router.post("/upload")
async def upload_media(
    file: UploadFile,
    session: AsyncSession = Depends(get_session)
):
    repo = MediaRepository(session)
    service = UploadMediaService(repo)

    result = await service.execute(UploadMediaCommand(file=file))
    return {"items": [item.id for item in result]}
