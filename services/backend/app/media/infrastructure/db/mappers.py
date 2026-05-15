from app.media.domain.entities import MediaItem, MediaType
from app.media.infrastructure.db.models import MediaItemModel


def model_to_domain(model: MediaItemModel) -> MediaItem:
    return MediaItem(
        id=model.id,
        type=MediaType(model.type.value),
        filename=model.filename,
        filepath=model.filepath,
        sha256=model.sha256,
        phash=model.phash,
        size_bytes=model.size_bytes,
        width=model.width,
        height=model.height,
        duration=model.duration,
        created_at=model.created_at,
        ingested_at=model.ingested_at,
    )


def domain_to_model(entity: MediaItem) -> MediaItemModel:
    return MediaItemModel(
        id=entity.id,
        type=entity.type,
        filename=entity.filename,
        filepath=entity.filepath,
        sha256=entity.sha256,
        phash=entity.phash,
        size_bytes=entity.size_bytes,
        width=entity.width,
        height=entity.height,
        duration=entity.duration,
        created_at=entity.created_at,
        ingested_at=entity.ingested_at,
    )
