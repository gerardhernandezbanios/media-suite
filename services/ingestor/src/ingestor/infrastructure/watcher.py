# src/ingestor/infrastructure/watcher.py
import time
from pathlib import Path

from ingestor.application.service import IngestService
from ingestor.config import Config
from ingestor.infrastructure.logging.logger import get_logger
from ingestor.infrastructure.logging_csv import CsvIngestLogger
from watchdog.events import FileSystemEventHandler
from watchdog.observers.polling import PollingObserver as Observer

logger = get_logger(__name__)


class IngestEventHandler(FileSystemEventHandler):
    def __init__(self):
        csv_logger = CsvIngestLogger(Config.LOG_FILE)
        self.service = IngestService(csv_logger)

    def on_created(self, event):
        if not event.is_directory:
            logger.info(f"New file detected: {event.src_path}")
            self.service.process_file(Path(event.src_path))


def start_watcher():
    observer = Observer(timeout=5)  # polling cada 5 segundos
    handler = IngestEventHandler()

    observer.schedule(handler, str(Config.SOURCE_DIR), recursive=False)
    observer.start()

    logger.info(f"Watcher started for directory: {Config.SOURCE_DIR}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
