import os
from pathlib import Path


class Config:
    SOURCE_DIR = Path(os.getenv("SOURCE_DIR", "/data/incoming"))
    IMAGES_ROOT = Path(os.getenv("IMAGES_ROOT", "/data/photos"))
    VIDEOS_ROOT = Path(os.getenv("VIDEOS_ROOT", "/data/videos"))
    ANIMATIONS_ROOT = Path(os.getenv("ANIMATIONS_ROOT", "/data/animations"))
    LOG_FILE = Path(os.getenv("LOG_FILE", "/data/logs/file_movements.csv"))
    AUDIT_FILE = Path(os.getenv("AUDIT_FILE", "/data/logs/audit_summary.csv"))

    IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png"]
    VIDEO_EXTENSIONS = [".mp4", ".mov", ".avi", ".mkv"]
    ANIMATION_EXTENSIONS = [".gif"]

    SPECIAL_FOLDERS = {
        "collage": "collage",
        "effect": "effects",
        "screenshot": "screenshots"
    }
