from app.media.domain.entities import MediaItem, MediaType
from services.backend.app.media.infrastructure.db.media_metadata_model import MediaItemModel
from app.media.domain.entities import MediaMetadata
from services.backend.app.media.infrastructure.db.media_metadata_model import MediaMetadataModel

def media_item_from_model(model: MediaItemModel) -> MediaItem:
    return MediaItem(
        id=model.id,
        type=MediaType(model.type),
        original_path=model.original_path,
        final_path=MediaPath.from_str(model.final_path) if model.final_path else None,
        captured_at=model.captured_at,
        imported_at=model.imported_at,
        checksum=Checksum(model.checksum) if model.checksum else None,
        width=model.width,
        height=model.height,
        duration_seconds=model.duration_seconds,
        tags=[Tag(id=t.id, name=t.name) for t in model.tags]
    )

def media_item_to_model(entity: MediaItem) -> MediaItemModel:
    return MediaItemModel(
        id=entity.id,
        type=entity.type.value,
        original_path=entity.original_path,
        final_path=entity.final_path.as_str() if entity.final_path else None,
        captured_at=entity.captured_at,
        imported_at=entity.imported_at,
        checksum=entity.checksum.value if entity.checksum else None,
        width=entity.width,
        height=entity.height,
        duration_seconds=entity.duration_seconds,
    )

