#services/backend/app/media/api/upload.py
from fastapi import APIRouter, UploadFile

router = APIRouter()

@router.post("/upload")
async def upload_media(file: UploadFile):
    return {"status": "ok", "filename": file.filename}
