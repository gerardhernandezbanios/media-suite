# domain\mover.py
from pathlib import Path

from ingestor.domain.exif_reader import get_exif_date


def compute_destination(
    file: Path, root_dest: Path, special_folder: str | None
) -> Path:
    if special_folder:
        return root_dest / special_folder

    date = get_exif_date(file)
    year = str(date.year)
    month = f"{date.month:02d}"
    return root_dest / year / month


def compute_unique_name(dest_dir: Path, file: Path) -> Path:
    new_path = dest_dir / file.name
    counter = 1
    while new_path.exists():
        new_path = dest_dir / f"{file.stem}_{counter}{file.suffix}"
        counter += 1
    return new_path
