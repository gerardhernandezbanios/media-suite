# test/application/test_service.py
from ingestor.application.service import IngestService
from ingestor.config import Config
from ingestor.logging_base import IngestLogger


class FakeLogger(IngestLogger):
    def __init__(self):
        self.moves = []
        self.unsupported = []

    def log_move(self, src, dst, timestamp, zip_origin):
        self.moves.append((src, dst, zip_origin))

    def log_unsupported(self, file):
        self.unsupported.append(file)


def test_service_moves_image(tmp_path, monkeypatch):
    monkeypatch.setattr(Config, "IMAGES_ROOT", tmp_path / "images")

    file = tmp_path / "photo.jpg"
    file.write_text("x")

    logger = FakeLogger()
    service = IngestService(logger)

    service.process_file(file)

    assert len(logger.moves) == 1
    assert logger.moves[0][0] == file
    assert logger.moves[0][1].exists()
