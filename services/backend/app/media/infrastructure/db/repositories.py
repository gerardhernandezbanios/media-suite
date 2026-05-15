# services/backend/app/media/infrastructure/db/repositories.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.media.infrastructure.db.models import MediaItemModel
from app.media.infrastructure.db.mappers import model_to_domain


class MediaRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, model: MediaItemModel):
        self.session.add(model)
        await self.session.flush()
        return model_to_domain(model)

    async def get_by_id(self, media_id: int):
        stmt = select(MediaItemModel).where(MediaItemModel.id == media_id)
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()
        return model_to_domain(model) if model else None

    async def list(self, limit: int = 100):
        stmt = select(MediaItemModel).limit(limit)
        result = await self.session.execute(stmt)
        return [model_to_domain(m) for m in result.scalars().all()]
