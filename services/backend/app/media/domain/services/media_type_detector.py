# services/backend/app/media/domain/services/media_type_detector.py

from services.backend.app.media.domain.value_objects.media_type import MediaType

IMAGE_EXT = {"jpg", "jpeg", "png", "webp", "heic"}
VIDEO_EXT = {"mp4", "mov", "avi", "mkv"}

class MediaTypeDetectorAdapter():

    def detect(self, filename: str) -> MediaType:
        ext = filename.lower().split(".")[-1]

        if ext in IMAGE_EXT:
            return MediaType.PHOTO

        if ext in VIDEO_EXT:
            return MediaType.VIDEO

        raise ValueError(f"Extensión no soportada: {ext}")