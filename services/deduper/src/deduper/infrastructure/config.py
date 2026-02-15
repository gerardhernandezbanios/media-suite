# deduper/src/deduper/infrastructure/config.py

import os
from pathlib import Path
from typing import Optional


def get_env_path(var_name: str) -> Path:
    value: Optional[str] = os.getenv(var_name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable: {var_name}")
    return Path(value)


class Config:
    """
    Configuración del servicio Deduper.
    Sigue el mismo patrón que el servicio Ingestor.
    """

    # Rutas principales (compatibles con toda la suite)
    SOURCE_DIR: Path = get_env_path("SOURCE_DIR")
    IMAGES_ROOT: Path = get_env_path("IMAGES_ROOT")
    VIDEOS_ROOT: Path = get_env_path("VIDEOS_ROOT")
    ANIMATIONS_ROOT: Path = get_env_path("ANIMATIONS_ROOT")
    UNSUPPORTED_ROOT: Path = get_env_path("UNSUPPORTED_ROOT")

    # Ruta específica del deduper
    DUPLICATES_ROOT: Path = get_env_path("DUPLICATES_ROOT")

    # Logging (aunque deduper no los use directamente, mantenemos coherencia)
    LOG_FILE: Path = get_env_path("LOG_FILE")
    AUDIT_FILE: Path = get_env_path("AUDIT_FILE")

    @classmethod
    def validate(cls) -> None:
        """
        Valida que las rutas necesarias existen y son escribibles.
        Igual que en el servicio Ingestor.
        """
        required_dirs = [
            cls.DUPLICATES_ROOT,
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

        print("✔ Deduper configuration validated and directories ready")
