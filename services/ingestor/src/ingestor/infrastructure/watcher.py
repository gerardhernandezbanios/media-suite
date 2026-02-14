# ingestor/infrastructure/watcher.py
import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers.polling import PollingObserver as Observer

from ingestor.infrastructure.logging.logger import get_logger

logger = get_logger(__name__)

class IngestEventHandler(FileSystemEventHandler):
    def __init__(self, service, config):
        self.service = service
        self.config = config

    def on_created(self, event):
        if not event.is_directory:
            logger.info(f"New file detected: {event.src_path}")
            self.service.process_file(Path(event.src_path))


def start_watcher(service, config):
    observer = Observer(timeout=5)
    handler = IngestEventHandler(service, config)

    observer.schedule(handler, str(config.SOURCE_DIR), recursive=False)
    observer.start()

    logger.info(f"Watcher started for directory: {config.SOURCE_DIR}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
