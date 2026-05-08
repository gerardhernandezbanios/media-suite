from ingestor.application.service import IngestService
from ingestor.config import Config
from ingestor.infrastructure.logging_csv import CsvIngestLogger


def test_ingest_service_moves_files(tmp_path, monkeypatch):
    # Override config paths
    monkeypatch.setattr(Config, "SOURCE_DIR", tmp_path)
    monkeypatch.setattr(Config, "DEST_DIR", tmp_path / "dest")
    monkeypatch.setattr(Config, "LOG_FILE", tmp_path / "log.csv")

    logger = CsvIngestLogger(Config.LOG_FILE)
    service = IngestService(logger)

    # Create a fake image
    f = tmp_path / "photo.jpg"
    f.write_bytes(b"data")

    service.process_file(f)

    # Should be moved into dest/images/YYYY/MM
    dest_root = Config.DEST_DIR / "images"
    assert dest_root.exists()
