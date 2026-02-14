from unittest.mock import Mock
import pytest
from ingestor.application.service import IngestService


@pytest.fixture
def fs():
    return Mock()


@pytest.fixture
def config(tmp_path):
    class DummyConfig:
        IMAGES_ROOT = tmp_path / "images"
        VIDEOS_ROOT = tmp_path / "videos"
        ANIMATIONS_ROOT = tmp_path / "animations"
        UNSUPPORTED_ROOT = tmp_path / "unsupported"
        WATCH_ROOT = tmp_path / "watch"
        SOURCE_DIR = tmp_path / "source"

    cfg = DummyConfig()
    for p in [
        cfg.IMAGES_ROOT,
        cfg.VIDEOS_ROOT,
        cfg.ANIMATIONS_ROOT,
        cfg.UNSUPPORTED_ROOT,
        cfg.WATCH_ROOT,
        cfg.SOURCE_DIR,
    ]:
        p.mkdir(parents=True, exist_ok=True)

    return cfg

@pytest.fixture
def service(fs, config):
    return IngestService(
        logger=Mock(),
        inspector=Mock(inspect=lambda p: Mock(
            is_directory=False,
            is_archive=False
        )),
        classifier=Mock(classify=lambda info: "images"),
        renamer=Mock(normalize=lambda p: p),
        fs=fs,
        zip_extractor=Mock(),
        config=config,
    )

def test_ingest_directory(service, fs, config, tmp_path):
    src = tmp_path / "folder"
    src.mkdir()

    service.process_file(src)
    
    fs.move.assert_not_called()

def test_ingest_image(service, fs, config, tmp_path):
    src = tmp_path / "photo.JPG"
    src.touch()

    service.process_file(src)

    dst = config.IMAGES_ROOT / src.name
    fs.move.assert_called_once_with(src, dst)

