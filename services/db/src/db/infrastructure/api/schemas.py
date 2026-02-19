# infrastructure/api/schemas.py
from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional

class PhotoCreateDTO(BaseModel):
    path: str

class PhotoDTO(BaseModel):
    id: UUID
    path: str

    class Config:
        from_attributes = True

class PhotoTagsUpdateDTO(BaseModel):
    tags: List[str]

class PhotoHashesUpdateDTO(BaseModel):
    phash: Optional[str] = None
    ahash: Optional[str] = None
    dhash: Optional[str] = None