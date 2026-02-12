# domain\mover.py
from pathlib import Path

from ingestor.domain.exif_reader import get_exif_date


def compute_destination(file: Path, root_dest: Path, category: str) -> Path:
    """
    Devuelve la carpeta final: root/category/YYYY/MM
    """
    date = get_exif_date(file)
    year = str(date.year)
    month = f"{date.month:02d}"

    return root_dest / category / year / month


def compute_unique_name(dest_dir: Path, file: Path) -> Path:
    new_path = dest_dir / file.name
    counter = 1
    while new_path.exists():
        new_path = dest_dir / f"{file.stem}_{counter}{file.suffix}"
        counter += 1
    return new_path
