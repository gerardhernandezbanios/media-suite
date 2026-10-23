# services/backend/app/media/domain/value_objects/media_path.py

from dataclasses import dataclass

@dataclass(frozen=True)
class MediaPath:
    root: str      # p.ej. "/media"
    type_dir: str  # "photos" o "videos"
    year: int
    month: int
    filename: str

    def as_str(self) -> str:
        return f"{self.root}/{self.type_dir}/{self.year:04d}/{self.month:02d}/{self.filename}"
