#services/backend/app/media/api/media.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_media():
    return []
