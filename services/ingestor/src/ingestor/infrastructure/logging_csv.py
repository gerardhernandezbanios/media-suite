# src/ingestor/infrastructure/logging_csv.py
import csv
from datetime import datetime
from pathlib import Path

from ingestor.infrastructure.logging_base import IngestLogger


class CsvIngestLogger(IngestLogger):
    def __init__(self, log_file: Path):
        log_file.parent.mkdir(parents=True, exist_ok=True)
        self.log_file = log_file

    def _write_row(self, row: list[str]):
        with open(self.log_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(row)

    def log_move(self, src, dst, timestamp, zip_origin):
        self._write_row([str(src), str(dst), timestamp.isoformat(), zip_origin or ""])

    def log_unsupported(self, file):
        self._write_row([str(file), "unsupported", datetime.now().isoformat(), ""])
