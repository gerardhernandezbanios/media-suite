# services/backend/app/media/api/mappers.py

from app.media.domain.entities import MediaItem
from app.media.domain.value_objects import MediaType
from services.backend.app.media.application.dto.media_item_dto import MediaItemDTO

def media_item_to_dto(entity: MediaItem) -> MediaItemDTO:
    return MediaItemDTO(
        id=entity.id,
        type=entity.type.value,
        final_path=entity.final_path.as_str() if entity.final_path else None,
        captured_at=entity.captured_at,
        imported_at=entity.imported_at,
        width=entity.width,
        height=entity.height,
        duration_seconds=entity.duration_seconds,
        tags=[t.name for t in entity.tags]
    )

