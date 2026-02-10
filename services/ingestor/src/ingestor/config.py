# src/ingestor/config.py
import os
from pathlib import Path
from typing import Optional


def get_env_path(var_name: str) -> Path:
    value: Optional[str] = os.getenv(var_name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable: {var_name}")
    return Path(value)


class Config:
    SOURCE_DIR = get_env_path("SOURCE_DIR")
    IMAGES_ROOT = get_env_path("IMAGES_ROOT")
    VIDEOS_ROOT = get_env_path("VIDEOS_ROOT")
    ANIMATIONS_ROOT = get_env_path("ANIMATIONS_ROOT")
    LOG_FILE = get_env_path("LOG_FILE")
    AUDIT_FILE = get_env_path("AUDIT_FILE")

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
