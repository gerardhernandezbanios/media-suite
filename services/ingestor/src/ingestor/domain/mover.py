# ingestor/domain/mover.py
from pathlib import Path

from ingestor.domain.exif_reader import get_exif_date


def compute_destination(path: Path, root: Path) -> Path:
    # Usamos la fecha del fichero
    # ts = path.stat().st_mtime
    # dt = datetime.fromtimestamp(ts)

    # year = str(dt.year)
    # month = f"{dt.month:02d}"

    """
    Devuelve la carpeta final: root/YYYY/MM
    """
    date = get_exif_date(path)
    year = str(date.year)
    month = f"{date.month:02d}"

    # root ya viene de config vía IngestService
    dest = root / year / month
    dest.mkdir(parents=True, exist_ok=True)

    return dest


def compute_unique_name(dest_dir: Path, path: Path) -> Path:
    candidate = dest_dir / path.name
    if not candidate.exists():
        return candidate

    stem = path.stem
    suffix = path.suffix

    i = 1
    while True:
        new_name = dest_dir / f"{stem}_{i}{suffix}"
        if not new_name.exists():
            return new_name
        i += 1

# def compute_unique_name(dest_dir: Path, file: Path) -> Path:
#     new_path = dest_dir / file.name
#     counter = 1
#     while new_path.exists():
#         new_path = dest_dir / f"{file.stem}_{counter}{file.suffix}"
#         counter += 1
#     return new_path
