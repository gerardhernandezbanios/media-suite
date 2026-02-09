import json

from ingestor.config import Config
from ingestor.watcher import start_watcher


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
    print("Starting ingestor service...")
    dump_config()
    start_watcher()
