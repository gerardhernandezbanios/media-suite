# services/backend/app/media/api/upload.py
from __future__ import annotations

from fastapi import APIRouter, UploadFile, File
from dependency_injector.wiring import inject, Provide

from typing import Container, List

from services.backend.app.core.container import Container
from media.application.use_cases.upload_media_use_case import UploadMediaUseCase

router = APIRouter(prefix="/media", tags=["media"])

@router.post("/upload")
@inject
async def upload_media(
    files: List[UploadFile] = File(...),
    use_case: UploadMediaUseCase = Depends(Provide[Container.upload_media_use_case])
):
    job_id = await use_case.execute(files)
    return {"job_id": job_id, "status": "pending"}
