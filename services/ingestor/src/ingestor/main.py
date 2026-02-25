# ingestor/main.py
import asyncio
import json

from ingestor.application.service import IngestService
from ingestor.config import Config
from ingestor.domain.classifier import Classifier
from ingestor.domain.file_inspector import FileInspector
from ingestor.domain.renamer import Renamer
from ingestor.infrastructure.file_system import FileSystem
from ingestor.infrastructure.zip_extractor import ZipExtractor
from ingestor.infrastructure.logging.logger import setup_logging
from ingestor.infrastructure.logging_csv import CsvIngestLogger
from ingestor.infrastructure.watcher import start_watcher
from ingestor.infrastructure.db_client import build_photo_repository


def build_service():
    return IngestService(
        logger=CsvIngestLogger(Config.LOG_FILE),
        inspector=FileInspector(),
        classifier=Classifier(),
        renamer=Renamer(),
        fs=FileSystem(),
        zip_extractor=ZipExtractor(),
        config=Config,
        photo_repo=build_photo_repository(Config)
    )


def dump_config():
    config = {
        "SOURCE_DIR": str(Config.SOURCE_DIR),
        "IMAGES_ROOT": str(Config.IMAGES_ROOT),
        "VIDEOS_ROOT": str(Config.VIDEOS_ROOT),
        "ANIMATIONS_ROOT": str(Config.ANIMATIONS_ROOT),
        "LOG_FILE": str(Config.LOG_FILE),
        "AUDIT_FILE": str(Config.AUDIT_FILE),
        "DB_SERVICE_URL": str(Config.DB_SERVICE_URL),
    }
    print("Current configuration:")
    print(json.dumps(config, indent=4))


async def process_existing_files(service):
    for file in Config.SOURCE_DIR.iterdir():
        if file.is_file():
            await service.process_file(file)


async def run_async():
    print("🚀 Starting ingestor service...")

    Config.validate()
    dump_config()

    service = build_service()

    print("📂 Processing existing files...")
    await process_existing_files(service)

    print("👀 Starting watcher...")
    start_watcher(service, Config)


def run():
    asyncio.run(run_async())


if __name__ == "__main__":
    run()
