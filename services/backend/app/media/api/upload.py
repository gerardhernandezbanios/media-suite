#services/backend/app/media/api/upload.py
from __future__ import annotations

from typing import List

from fastapi import APIRouter, UploadFile, Depends

from app.media.application.services import UploadMediaService
from app.shared.dto.media import MediaItemDTO
from app.core.container import container
from services.backend.app.media.application.dto.uploaded_file_dto import UploadedFileDTO

router = APIRouter(prefix="/media", tags=["media"])


# def get_upload_service() -> UploadMediaService:
#     return container.upload_media_service()

# @router.post("/upload", response_model=List[MediaItemDTO])
# async def upload_media(
#     files: List[UploadFile],
#     service: UploadMediaService = Depends(get_upload_service),
# ) -> List[MediaItemDTO]:
#     return await service.handle(files)

@router.post("/media/upload")
async def upload_media(files: list[UploadFile], uc: UploadMediaUseCase = Depends()):
    dtos = [UploadedFileDTO.from_uploadfile(f) for f in files]
    result = await uc.execute(dtos)
    return result
