# test/infrastructure/test_logging_csv.py
from datetime import datetime

from ingestor.infrastructure.logging_csv import CsvIngestLogger


def test_csv_logger_writes_rows(tmp_path):
    log_file = tmp_path / "log.csv"
    logger = CsvIngestLogger(log_file)

    src = tmp_path / "src.jpg"
    dst = tmp_path / "dst.jpg"
    timestamp = datetime(2024, 1, 1)

    logger.log_move(src, dst, timestamp, "zip1")

    content = log_file.read_text()
    assert "src.jpg" in content
    assert "dst.jpg" in content
    assert "2024-01-01" in content
    assert "zip1" in content
