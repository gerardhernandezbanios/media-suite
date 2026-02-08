from pathlib import Path

from ingestor.config import Config


def classify(file: Path):
    ext = file.suffix.lower()

    if ext in Config.IMAGE_EXTENSIONS:
        return "image"
    if ext in Config.VIDEO_EXTENSIONS:
        return "video"
    if ext in Config.ANIMATION_EXTENSIONS:
        return "animation"
    if ext == ".zip":
        return "zip"
    return "unsupported"
