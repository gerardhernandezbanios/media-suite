from .config import Config
from .file_classifier import classify
from .mover import move_file
from .zip_processor import process_zip
from .stats import Stats
import csv

def run():
    with open(Config.LOG_FILE, "w", newline="", encoding="utf-8") as log:
        writer = csv.writer(log)
        writer.writerow(["Source", "Destination", "Timestamp", "ZipOrigin"])

        for file in Config.SOURCE_DIR.iterdir():
            if not file.is_file():
                continue

            file_type = classify(file)

            if file_type == "image":
                move_file(file, Config.IMAGES_ROOT, writer)
            elif file_type == "video":
                move_file(file, Config.VIDEOS_ROOT, writer)
            elif file_type == "animation":
                move_file(file, Config.ANIMATIONS_ROOT, writer)
            elif file_type == "zip":
                continue
            else:
                Stats.global_stats["unsupported"] += 1

        for file in Config.SOURCE_DIR.iterdir():
            if file.is_file() and file.suffix.lower() == ".zip":
                process_zip(file, writer)

    Stats.write_audit(Config.AUDIT_FILE)
