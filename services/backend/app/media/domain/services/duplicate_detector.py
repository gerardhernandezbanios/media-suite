# services/backend/app/media/domain/services/duplicate_detector.py
from typing import Iterable
from .entities import MediaItem

class DuplicateDetector:
    def find_duplicates(self, items: Iterable[MediaItem]) -> dict[str, list[MediaItem]]:
        by_checksum: dict[str, list[MediaItem]] = {}
        for item in items:
            if not item.checksum:
                continue
            key = item.checksum.value
            by_checksum.setdefault(key, []).append(item)
        return {k: v for k, v in by_checksum.items() if len(v) > 1}
