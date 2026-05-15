#services/backend/app/media/infrastructure/db/models.py
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


class MediaItemModel(Base):
    __tablename__ = "media_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    type: Mapped[MediaType] = mapped_column(Enum(MediaType), nullable=False)

    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    filepath: Mapped[str] = mapped_column(String(500), nullable=False)

    sha256: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    phash: Mapped[str | None] = mapped_column(String(32), nullable=True)

    size_bytes: Mapped[int] = mapped_column(Integer, nullable=False)
    width: Mapped[int | None] = mapped_column(Integer)
    height: Mapped[int | None] = mapped_column(Integer)
    duration: Mapped[float | None] = mapped_column(Float)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    ingested_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    tags: Mapped[list["MediaTagModel"]] = relationship(back_populates="media_item")

    __table_args__ = (
        Index("idx_media_sha256", "sha256"),
        Index("idx_media_type", "type"),
    )


class AlbumModel(Base):
    __tablename__ = "albums"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    items: Mapped[list["AlbumMediaModel"]] = relationship(back_populates="album")


class TagModel(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    media_items: Mapped[list["MediaTagModel"]] = relationship(back_populates="tag")


class MediaTagModel(Base):
    __tablename__ = "media_tags"

    media_id: Mapped[int] = mapped_column(
        ForeignKey("media_items.id", ondelete="CASCADE"), primary_key=True
    )
    tag_id: Mapped[int] = mapped_column(
        ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True
    )

    media_item: Mapped["MediaItemModel"] = relationship(back_populates="tags")
    tag: Mapped["TagModel"] = relationship(back_populates="media_items")


class AlbumMediaModel(Base):
    __tablename__ = "album_media"

    album_id: Mapped[int] = mapped_column(
        ForeignKey("albums.id", ondelete="CASCADE"), primary_key=True
    )
    media_id: Mapped[int] = mapped_column(
        ForeignKey("media_items.id", ondelete="CASCADE"), primary_key=True
    )

    album: Mapped["AlbumModel"] = relationship(back_populates="items")
    media_item: Mapped["MediaItemModel"] = relationship()
