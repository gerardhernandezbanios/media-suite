from uuid import UUID
from shared.domain.photo import Photo
from shared.domain.repositories import PhotoRepository
from shared.exceptions.errors import NotFoundError, DbServiceError

class PhotoApiClient(PhotoRepository):

    def __init__(self, http_client):
        self.http = http_client

    async def register_photo(self, path: str) -> Photo:
        r = await self.http.post("/photos", json={"path": path})
        if r.status_code == 404:
            raise NotFoundError("Photo not found")
        if r.status_code >= 400:
            raise DbServiceError(r.text)
        data = r.json()
        return Photo(id=data["id"], path=data["path"])

    async def register_photos(self, paths: list[str]) -> list[Photo]:
        r = await self.http.post("/photos/batch", json={"paths": paths})
        if r.status_code >= 400:
            raise DbServiceError(r.text)
        return [Photo(id=p["id"], path=p["path"]) for p in r.json()]

    async def update_hashes(self, photo_id: UUID, phash: str, ahash: str, dhash: str):
        r = await self.http.post(f"/photos/{photo_id}/hashes", json={
            "phash": phash,
            "ahash": ahash,
            "dhash": dhash
        })
        if r.status_code >= 400:
            raise DbServiceError(r.text)

    async def update_tags(self, photo_id: UUID, tags: list[str]):
        r = await self.http.post(f"/photos/{photo_id}/tags", json={"tags": tags})
        if r.status_code >= 400:
            raise DbServiceError(r.text)
