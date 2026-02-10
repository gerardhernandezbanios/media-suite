# src/ingestor/infrastructure/logging_base.py
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path


class IngestLogger(ABC):
    @abstractmethod
    def log_move(
        self, src: Path, dst: Path, timestamp: datetime, zip_origin: str | None
    ):
        """Log a successful file move."""
        pass

    @abstractmethod
    def log_unsupported(self, file: Path):
        """Log a file that could not be processed."""
        pass
