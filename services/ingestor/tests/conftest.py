import pytest
from ingestor import config

@pytest.fixture(autouse=True)
def patch_config(tmp_path, monkeypatch):
    monkeypatch.setattr(config.Config, "LOG_FILE", tmp_path / "logs" / "file_movements.csv")
    monkeypatch.setattr(config.Config, "AUDIT_FILE", tmp_path / "logs" / "audit_summary.csv")
    monkeypatch.setattr(config.Config, "SOURCE_DIR", tmp_path / "incoming")
    monkeypatch.setattr(config.Config, "IMAGES_ROOT", tmp_path / "images")
    monkeypatch.setattr(config.Config, "VIDEOS_ROOT", tmp_path / "videos")
    monkeypatch.setattr(config.Config, "ANIMATIONS_ROOT", tmp_path / "animations")
