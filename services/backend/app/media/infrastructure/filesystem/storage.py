# services/backend/app/media/infrastructure/filesystem/storage.py
import shutil
from pathlib import Path
from datetime import datetime
from app.core.config import settings


class FilesystemStorage:

    def __init__(self):
        self.media_root = Path(settings.MEDIA_ROOT)
        self.temp_root = self.media_root / "_temp"
        self.temp_root.mkdir(parents=True, exist_ok=True)

    def save_temp(self, file, filename: str) -> Path:
        """Guarda el archivo subido en una carpeta temporal."""
        temp_path = self.temp_root / filename
        with temp_path.open("wb") as f:
            shutil.copyfileobj(file.file, f)
        return temp_path

    def move_to_final_location(self, temp_path: Path, media_type: str, created_at: datetime) -> Path:
        """Mueve el archivo a /media/{image|video}/{año}/{mes}/filename"""
        year = str(created_at.year)
        month = f"{created_at.month:02d}"

        final_dir = self.media_root / media_type / year / month
        final_dir.mkdir(parents=True, exist_ok=True)

        final_path = final_dir / temp_path.name
        shutil.move(str(temp_path), final_path)

        return final_path
