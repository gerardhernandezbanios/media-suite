# services/backend/app/media/domain/services/exif_reader.py
from abc import ABC, abstractmethod
from typing import Optional
from datetime import datetime

class ExifData:
    captured_at: Optional[datetime]
    width: Optional[int]
    height: Optional[int]
    duration_seconds: Optional[float]

class ExifReader(ABC):
    @abstractmethod
    async def read(self, path: str) -> ExifData:
        ...
