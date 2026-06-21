# services/backend/app/media/infrastructure/db/repositories.py
from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from app.media.domain.entities import MediaItem
from services.backend.app.media.domain.repositories.repositories import MediaItemRepository
from app.media.infrastructure.db.models import MediaItemModel, MediaMetadataModel
from app.media.infrastructure.db.mappers import (
    domain_to_model,
    model_to_domain,
    metadata_domain_to_model,
)


class SqlAlchemyMediaItemRepository(MediaItemRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, item: MediaItem) -> MediaItem:
        model: MediaItemModel = domain_to_model(item)
        self.session.add(model)

        if getattr(item, "metadata", None) is not None:
            meta_model: MediaMetadataModel = metadata_domain_to_model(item.metadata)
            meta_model.media_item = model
            self.session.add(meta_model)

        await self.session.flush()
        await self.session.refresh(model)
        return model_to_domain(model)
