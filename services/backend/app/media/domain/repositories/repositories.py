
# services/backend/app/media/domain/repositories.py
from __future__ import annotations

from typing import Protocol

from services.backend.app.media.domain.entities import MediaItem


class MediaItemRepository(Protocol):
    async def save(self, item: MediaItem) -> MediaItem: ...
