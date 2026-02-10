# src/ingestor/config.py
import os
from pathlib import Path


class Config:
    SOURCE_DIR = Path(os.getenv("SOURCE_DIR"))
    IMAGES_ROOT = Path(os.getenv("IMAGES_ROOT"))
    VIDEOS_ROOT = Path(os.getenv("VIDEOS_ROOT"))
    ANIMATIONS_ROOT = Path(os.getenv("ANIMATIONS_ROOT"))
    LOG_FILE = Path(os.getenv("LOG_FILE"))
    AUDIT_FILE = Path(os.getenv("AUDIT_FILE"))

    IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png"]
    VIDEO_EXTENSIONS = [".mp4", ".mov", ".avi", ".mkv"]
    ANIMATION_EXTENSIONS = [".gif"]

    SPECIAL_FOLDERS = {
        "collage": "collage",
        "effect": "effects",
        "screenshot": "screenshots",
    }

    @classmethod
    def validate(cls):
        required_dirs = [
            cls.SOURCE_DIR,
            cls.IMAGES_ROOT,
            cls.VIDEOS_ROOT,
            cls.ANIMATIONS_ROOT,
            cls.LOG_FILE.parent,
            cls.AUDIT_FILE.parent,
        ]

        missing = [str(p) for p in required_dirs if not p.exists()]

        if missing:
            raise RuntimeError(
                "❌ Configuración inválida. Faltan directorios:\n"
                + "\n".join(f" - {m}" for m in missing)
            )


# class Config:
#     SOURCE_DIR = Path(os.getenv("SOURCE_DIR", "/data/incoming"))
#     IMAGES_ROOT = Path(os.getenv("IMAGES_ROOT", "/data/photos"))
#     VIDEOS_ROOT = Path(os.getenv("VIDEOS_ROOT", "/data/videos"))
#     ANIMATIONS_ROOT = Path(os.getenv("ANIMATIONS_ROOT", "/data/animations"))
#     LOG_FILE = Path(os.getenv("LOG_FILE", "/data/logs/file_movements.csv"))
#     AUDIT_FILE = Path(os.getenv("AUDIT_FILE", "/data/logs/audit_summary.csv"))
