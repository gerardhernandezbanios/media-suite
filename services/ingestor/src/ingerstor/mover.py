import shutil
from datetime import datetime
from pathlib import Path

from .exif import get_exif_date
from .stats import Stats


def move_file(file: Path, root_dest: Path, log_writer, special_folder=None, zip_origin=None):
    if special_folder:
        dest = root_dest / special_folder
    else:
        date = get_exif_date(file)
        year, month = str(date.year), f"{date.month:02d}"
        dest = root_dest / year / month
        Stats.update_by_month(file, year, month)

    dest.mkdir(parents=True, exist_ok=True)

    new_name = dest / file.name
    counter = 1
    while new_name.exists():
        new_name = dest / f"{file.stem}_{counter}{file.suffix}"
        counter += 1

    shutil.move(str(file), new_name)
    log_writer.writerow([file, new_name, datetime.now().isoformat(), zip_origin or ""])
    Stats.update_global(file, special_folder)
