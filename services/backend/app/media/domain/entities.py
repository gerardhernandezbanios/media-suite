#services/backend/app/media/domain/entities.py
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from enum import Enum


class MediaType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"


@dataclass
class MediaItem:
    id: Optional[int]
    type: MediaType
    filename: str
    filepath: str
    sha256: str
    phash: Optional[str]
    size_bytes: int
    width: Optional[int]
    height: Optional[int]
    duration: Optional[float]
    created_at: datetime
    ingested_at: datetime


@dataclass
class Album:
    id: Optional[int]
    name: str
    created_at: datetime


@dataclass
class Tag:
    id: Optional[int]
    name: str
