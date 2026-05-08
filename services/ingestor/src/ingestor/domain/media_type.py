from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from ingestor.config import Config


class MediaKind(Enum):
    IMAGE = "image"
    VIDEO = "video"
    ANIMATION = "animation"
    UNSUPPORTED = "unsupported"


@dataclass(frozen=True)
class MediaType:
    kind: MediaKind

    # -----------------------------
    # Factorías explícitas (DDD)
    # -----------------------------
    @staticmethod
    def image() -> "MediaType":
        return MediaType(MediaKind.IMAGE)

    @staticmethod
    def video() -> "MediaType":
        return MediaType(MediaKind.VIDEO)

    @staticmethod
    def animation() -> "MediaType":
        return MediaType(MediaKind.ANIMATION)

    @staticmethod
    def unsupported() -> "MediaType":
        return MediaType(MediaKind.UNSUPPORTED)

    @staticmethod
    def from_extension(ext: str) -> "MediaType":
        if not ext:
            return MediaType.unsupported()

        ext = ext.lower().lstrip(".")

        image_exts = [e.lower().lstrip(".") for e in Config.IMAGE_EXTENSIONS]
        video_exts = [e.lower().lstrip(".") for e in Config.VIDEO_EXTENSIONS]
        anim_exts = [e.lower().lstrip(".") for e in Config.ANIMATION_EXTENSIONS]

        if ext in image_exts:
            return MediaType.image()

        if ext in video_exts:
            return MediaType.video()

        if ext in anim_exts:
            return MediaType.animation()

        return MediaType.unsupported()

    @staticmethod
    def from_file(file: Path) -> "MediaType":
        return MediaType.from_extension(file.suffix)

    # -----------------------------
    # Métodos de intención (DDD)
    # -----------------------------
    def is_image(self) -> bool:
        return self.kind is MediaKind.IMAGE

    def is_video(self) -> bool:
        return self.kind is MediaKind.VIDEO

    def is_animation(self) -> bool:
        return self.kind is MediaKind.ANIMATION

    def is_supported(self) -> bool:
        return self.kind is not MediaKind.UNSUPPORTED
