# src/ingestor/main.py
import json

from ingestor.application.service import IngestService
from ingestor.config import Config
from ingestor.infrastructure.logging.logger import setup_logging
from ingestor.infrastructure.watcher import start_watcher

logger = setup_logging()


def dump_config():
    config = {
        "SOURCE_DIR": str(Config.SOURCE_DIR),
        "IMAGES_ROOT": str(Config.IMAGES_ROOT),
        "VIDEOS_ROOT": str(Config.VIDEOS_ROOT),
        "ANIMATIONS_ROOT": str(Config.ANIMATIONS_ROOT),
        "LOG_FILE": str(Config.LOG_FILE),
        "AUDIT_FILE": str(Config.AUDIT_FILE),
    }
    print("Current configuration:")
    print(json.dumps(config, indent=4))


def process_existing_files():
    service = IngestService(logger)
    for file in Config.SOURCE_DIR.iterdir():
        if file.is_file():
            logger.info(f"Processing existing file: {file}")
            service.process_file(file)


def run():
    print("🚀 Starting ingestor service...")

    Config.validate()
    dump_config()

    print("📂 Processing existing files...")
    process_existing_files()

    print("👀 Starting watcher...")
    start_watcher()


if __name__ == "__main__":
    run()
