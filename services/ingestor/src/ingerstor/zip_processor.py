import zipfile
import shutil
from pathlib import Path
from .config import Config
from .mover import move_file
from .file_classifier import classify
from .stats import Stats

def process_zip(file: Path, log_writer):
    tmp_dir = Config.SOURCE_DIR / f"tmp_zip_{file.stem}"
    tmp_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(file, "r") as zip_ref:
        zip_ref.extractall(tmp_dir)

    for extracted in tmp_dir.iterdir():
        if not extracted.is_file():
            continue

        file_type = classify(extracted)

        if file_type == "image":
            move_file(extracted, Config.IMAGES_ROOT, log_writer, zip_origin=file.name)
        elif file_type == "video":
            move_file(extracted, Config.VIDEOS_ROOT, log_writer, zip_origin=file.name)
        elif file_type == "animation":
            move_file(extracted, Config.ANIMATIONS_ROOT, log_writer, zip_origin=file.name)
        else:
            Stats.global_stats["unsupported"] += 1

    shutil.rmtree(tmp_dir)
    file.unlink()
