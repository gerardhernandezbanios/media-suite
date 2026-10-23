# services/backend/app/media/infrastructure/db/media_item_model.py

from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Enum, ForeignKey, Float, DateTime, Index
from app.media.domain.entities import MediaType

class Base(DeclarativeBase):
    pass

class MediaItemModel(Base):
    __tablename__ = "media_items"

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    original_path = Column(String, nullable=False)
    final_path = Column(String, nullable=True)
    captured_at = Column(DateTime, nullable=False)
    imported_at = Column(DateTime, nullable=False)
    checksum = Column(String, nullable=True)

    width = Column(Integer)
    height = Column(Integer)
    duration_seconds = Column(Float)

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
