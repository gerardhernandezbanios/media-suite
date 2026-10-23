#services/backend/app/media/api/albums.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_albums():
    return []
