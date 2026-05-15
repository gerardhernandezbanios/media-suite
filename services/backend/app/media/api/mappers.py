from app.media.domain.entities import MediaItem
from app.shared.dto.media import MediaItemDTO, MediaTypeDTO


def domain_to_dto(entity: MediaItem) -> MediaItemDTO:
    return MediaItemDTO(
        id=entity.id,
        type=MediaTypeDTO(entity.type.value),
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
