# infrstructure/db/mappers.py
from db.domain.models import Photo
from .models import PhotoORM

def photo_orm_to_domain(photo: PhotoORM) -> Photo:
    return Photo(
        id=photo.id,
        path=photo.path,
        created_at=photo.created_at,
        updated_at=photo.updated_at,
        tags=[t.tag for t in photo.tags],
        phash=photo.hashes.phash if photo.hashes else None,
        ahash=photo.hashes.ahash if photo.hashes else None,
        dhash=photo.hashes.dhash if photo.hashes else None,
    )