#services/backend/app/media/api/upload.py
from fastapi import APIRouter, UploadFile, Depends
from services.backend.app.shared.dto.media import MediaItemDTO
from sqlalchemy.ext.asyncio import AsyncSession

from app.media.application.commands import UploadMediaCommand, UploadMediaService
from app.media.infrastructure.db.repositories import MediaRepository
from app.core.db import get_session  # lo creamos ahora

from fastapi import APIRouter, UploadFile, Depends
from app.media.application.services import UploadMediaService

router = APIRouter()

@router.post("/upload", response_model=list[MediaItemDTO])
async def upload_media(
    files: list[UploadFile],
    service: UploadMediaService = Depends(),
):
    return await service.handle(files)


# router = APIRouter()


# @router.post("/upload")
# async def upload_media(
#     file: UploadFile,
#     session: AsyncSession = Depends(get_session)
# ):
#     repo = MediaRepository(session)
#     service = UploadMediaService(repo)

#     result = await service.execute(UploadMediaCommand(file=file))
#     return {"items": [item.id for item in result]}
