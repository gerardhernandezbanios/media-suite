# infrstructure/api/routes.py
from fastapi import APIRouter, Depends, HTTPException, Query
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from db.infrastructure.db.base import get_session
from db.application.use_cases import (
    register_photo,
    register_photos_batch,
    update_photo_hashes,
    update_photo_tags,
    get_photo_by_id,
    get_photo_by_path,
)
from db.infrastructure.db.repositories import PhotoRepository
from db.domain.models import Photo
from shared.dto.schemas import (
    PhotoBatchCreateDTO,
    PhotoCreateDTO,
    PhotoDTO,
    PhotoTagsUpdateDTO,
    PhotoHashesUpdateDTO
)

router = APIRouter()

@router.post("/photos", response_model=PhotoDTO)
async def create_photo(dto: PhotoCreateDTO, session: AsyncSession = Depends(get_session)):
    photo = await register_photo(dto.path, session)
    return PhotoDTO(id=photo.id, path=photo.path)

@router.post("/photos/batch", response_model=list[PhotoDTO])
async def create_photos_batch(
    dto: PhotoBatchCreateDTO,
    session: AsyncSession = Depends(get_session)
):
    photos = await register_photos_batch(dto.paths, session)
    return [PhotoDTO(id=p.id, path=p.path) for p in photos]

@router.get("/photos/{photo_id}", response_model=PhotoDTO)
async def get_photo(photo_id: UUID, session: AsyncSession = Depends(get_session)):
    photo = await get_photo_by_id(photo_id, session)
    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    return PhotoDTO(id=photo.id, path=photo.path)

@router.get("/photos/by-path", response_model=PhotoDTO)
async def get_photo_by_path_endpoint(path: str = Query(...), session: AsyncSession = Depends(get_session)):
    photo = await get_photo_by_path(path, session)
    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")
    return PhotoDTO(id=photo.id, path=photo.path)

@router.post("/photos/{photo_id}/tags")
async def update_tags(photo_id: UUID, dto: PhotoTagsUpdateDTO, session: AsyncSession = Depends(get_session)):
    await update_photo_tags(photo_id, dto.tags, session)
    return {"status": "ok"}

@router.post("/photos/{photo_id}/hashes")
async def update_hashes(photo_id: UUID, dto: PhotoHashesUpdateDTO, session: AsyncSession = Depends(get_session)):
    await update_photo_hashes(photo_id, dto.phash, dto.ahash, dto.dhash, session)
    return {"status": "ok"}
