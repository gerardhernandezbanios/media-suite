# services/backend/app/media/domain/services/media_type_detector.py
from services.backend.app.media.domain.value_objects.media_type import MediaType


class MediaTypeDetector:
    def detect(self, filename: str) -> MediaType:
        ext = filename.lower().split(".")[-1]
        if ext in ("jpg", "jpeg", "png", "heic", "webp"):
            return MediaType.PHOTO
        if ext in ("mp4", "mov", "avi", "mkv"):
            return MediaType.VIDEO
        raise ValueError(f"Extensión no soportada: {ext}")
