import csv
import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from ingestor.config import Config
from ingestor.file_classifier import classify
from ingestor.mover import move_file
from ingestor.stats import Stats
from ingestor.zip_processor import process_zip


class IngestEventHandler(FileSystemEventHandler):
    def __init__(self):
        self.log_file = Config.LOG_FILE
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

    def on_created(self, event):
        if event.is_directory:
            return

        file = Path(event.src_path)
        file_type = classify(file)

        with open(self.log_file, "a", newline="", encoding="utf-8") as log:
            writer = csv.writer(log)

            if file_type == "image":
                move_file(file, Config.IMAGES_ROOT, writer)
            elif file_type == "video":
                move_file(file, Config.VIDEOS_ROOT, writer)
            elif file_type == "animation":
                move_file(file, Config.ANIMATIONS_ROOT, writer)
            elif file_type == "zip":
                process_zip(file, writer)
            else:
                Stats.global_stats["unsupported"] += 1


def start_watcher():
    observer = Observer()
    handler = IngestEventHandler()

    observer.schedule(handler, str(Config.SOURCE_DIR), recursive=False)
    observer.start()

    print(f"Watching for new files in: {Config.SOURCE_DIR}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
