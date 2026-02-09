# infraestructure/watcher.py
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from ingestor.application.service import IngestService
from ingestor.infraestructure.logging_csv import CsvIngestLogger
from ingestor.config import Config
import time

class IngestEventHandler(FileSystemEventHandler):
    def __init__(self):
        logger = CsvIngestLogger(Config.LOG_FILE)
        self.service = IngestService(logger)

    def on_created(self, event):
        if not event.is_directory:
            self.service.process_file(Path(event.src_path))


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
