# src/ingestor/main.py
import json

from ingestor.config import Config
from ingestor.infrastructure.logging.logger import setup_logging
from ingestor.infrastructure.watcher import start_watcher

logger = setup_logging()


def dump_config():
    config_path = Config.LOG_FILE.parent / "service_config.json"
    config = {
        "SOURCE_DIR": str(Config.SOURCE_DIR),
        "IMAGES_ROOT": str(Config.IMAGES_ROOT),
        "VIDEOS_ROOT": str(Config.VIDEOS_ROOT),
        "ANIMATIONS_ROOT": str(Config.ANIMATIONS_ROOT),
        "LOG_FILE": str(Config.LOG_FILE),
        "AUDIT_FILE": str(Config.AUDIT_FILE),
    }
    config_path.write_text(json.dumps(config, indent=4))


def run():
    logger.info("Starting ingestor service...")

    logger.debug("Validating configuration...")
    Config.validate()
    logger.debug("✔ Configuration OK")

    dump_config()
    logger.debug("✔ Configuration dumped")

    logger.info("Starting watcher...")
    start_watcher()
