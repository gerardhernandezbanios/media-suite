# services/backend/app/media/domain/value_objects/media_type.py

from enum import Enum

class MediaType(str, Enum):
    PHOTO = "photo"
    VIDEO = "video"
