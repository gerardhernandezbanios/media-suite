# services/backend/app/media/api/upload.py
from __future__ import annotations

from fastapi import APIRouter, UploadFile, File
from typing import List
from media.application.use_cases.upload_media_use_case import UploadMediaUseCase

router = APIRouter(prefix="/media", tags=["media"])

@router.post("/upload")
async def upload_media(files: List[UploadFile] = File(...)):
    use_case = UploadMediaUseCase(job_port=...)  # inyectado desde container
    job_id = await use_case.execute(files)
    return {"job_id": job_id, "status": "pending"}
