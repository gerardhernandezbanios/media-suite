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
    # Directorios principales
    SOURCE_DIR: Path = get_env_path("SOURCE_DIR")
    IMAGES_ROOT: Path = get_env_path("IMAGES_ROOT")
    VIDEOS_ROOT: Path = get_env_path("VIDEOS_ROOT")
    ANIMATIONS_ROOT: Path = get_env_path("ANIMATIONS_ROOT")
    UNSUPPORTED_ROOT: Path = get_env_path("UNSUPPORTED_ROOT")

    # Logging
    LOG_FILE: Path = get_env_path("LOG_FILE")
    AUDIT_FILE: Path = get_env_path("AUDIT_FILE")

    # Extensiones soportadas
    IMAGE_EXTENSIONS: list[str] = [
        "jpg",
        "jpeg",
        "jpe",
        "jfif",
        "png",
        "bmp",
        "tif",
        "tiff",
        "heic",
        "heif",
        "raw",
        "arw",
        "cr2",
        "nef",
        "orf",
        "sr2",
        "ppm",
        "pgm",
        "pbm",
        "pnm",
        "svg",
    ]

    VIDEO_EXTENSIONS: list[str] = [
        "mp4",
        "m4v",
        "mov",
        "avi",
        "mkv",
        "webm",
        "flv",
        "wmv",
        "mpeg",
        "mpg",
        "mpe",
        "3gp",
        "3g2",
        "mts",
        "m2ts",
        "ts",
    ]

    ANIMATION_EXTENSIONS: list[str] = ["gif", "apng", "webp"]

    ARCHIVE_EXTENSIONS: list[str] = ["zip", "rar", "7z", "tar", "gz"]

    @classmethod
    def validate(cls) -> None:
        required_dirs = [
            cls.SOURCE_DIR,
            cls.IMAGES_ROOT,
            cls.VIDEOS_ROOT,
            cls.ANIMATIONS_ROOT,
            cls.UNSUPPORTED_ROOT,
            cls.LOG_FILE.parent,
            cls.AUDIT_FILE.parent,
        ]

        # Crear directorios faltantes
        for p in required_dirs:
            if not p.exists():
                try:
                    p.mkdir(parents=True, exist_ok=True)
                    print(f"✔ Created missing directory: {p}")
                except Exception as e:
                    raise RuntimeError(f"❌ Cannot create directory {p}: {e}")

        # Comprobar permisos de escritura
        for p in required_dirs:
            try:
                test_file = p / ".write_test"
                test_file.write_text("ok")
                test_file.unlink()
            except Exception as e:
                raise RuntimeError(f"❌ No write permission in {p}: {e}")

        print("✔ Configuration validated and directories ready")
