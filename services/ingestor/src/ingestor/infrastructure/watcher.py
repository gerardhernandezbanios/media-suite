# ingestor/infrastructure/watcher.py
import time
from pathlib import Path

from ingestor.infrastructure.logging.logger import get_logger
from watchdog.events import FileSystemEventHandler
from watchdog.observers.polling import PollingObserver as Observer

logger = get_logger(__name__)

# class IngestEventHandler(FileSystemEventHandler):
#     def __init__(self, service, config):
#         self.service = service
#         self.config = config

#     def on_created(self, event):
#         if not event.is_directory:
#             logger.info(f"New file detected: {event.src_path}")

#             # Ejecutamos la corutina sin bloquear watchdog
#             asyncio.create_task(
#                 self.service.process_file(Path(event.src_path))
#             )

class IngestEventHandler(FileSystemEventHandler):
    def __init__(self, service, config):
        self.service = service
        self.config = config

    def on_created(self, event):
        path = Path(event.src_path)

        if path.is_file():
            logger.info(f"New file detected: {path}")
            self.service.process_file(path)

        elif path.is_dir():
            logger.info(f"New directory detected: {path}")
            self._process_directory(path)

    def _process_directory(self, directory: Path):
        for item in directory.iterdir():
            if item.is_file():
                logger.info(f"Processing file inside directory: {item}")
                self.service.process_file(item)

            elif item.is_dir():
                logger.info(f"Descending into subdirectory: {item}")
                self._process_directory(item)


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
