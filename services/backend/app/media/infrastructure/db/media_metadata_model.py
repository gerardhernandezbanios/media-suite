# services/backend/app/media/infrastructure/db/media_metadata_model.py
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Enum, ForeignKey, Float, DateTime, Index
from app.media.domain.entities import MediaType


class Base(DeclarativeBase):
    pass

class MediaMetadataModel(Base):
    __tablename__ = "media_metadata"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    media_id: Mapped[int] = mapped_column(
        ForeignKey("media_items.id", ondelete="CASCADE"), unique=True
    )

    # Imagen
    width: Mapped[int | None]
    height: Mapped[int | None]
    orientation: Mapped[int | None]

    # EXIF
    camera_make: Mapped[str | None]
    camera_model: Mapped[str | None]
    lens_model: Mapped[str | None]
    iso: Mapped[int | None]
    aperture: Mapped[float | None]
    shutter_speed: Mapped[str | None]
    focal_length: Mapped[float | None]
    created_at: Mapped[datetime | None]

    # Vídeo
    duration: Mapped[float | None]
    video_codec: Mapped[str | None]
    audio_codec: Mapped[str | None]
    frame_rate: Mapped[float | None]
    bit_rate: Mapped[int | None]

    media_item: Mapped["MediaItemModel"] = relationship(back_populates="metadata")
