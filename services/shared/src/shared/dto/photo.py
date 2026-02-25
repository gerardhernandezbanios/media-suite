from pydantic import BaseModel
from uuid import UUID

class PhotoDTO(BaseModel):
    id: UUID
    path: str

class PhotoCreateDTO(BaseModel):
    path: str

class PhotoBatchCreateDTO(BaseModel):
    paths: list[str]

class PhotoHashesUpdateDTO(BaseModel):
    phash: str | None = None
    ahash: str | None = None
    dhash: str | None = None

class PhotoTagsUpdateDTO(BaseModel):
    tags: list[str]
