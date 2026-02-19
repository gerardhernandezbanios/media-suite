# infrstructure/db/models.py
from sqlalchemy import Column, Text, TIMESTAMP, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .base import Base

class PhotoORM(Base):
    __tablename__ = "photos"

    id = Column(UUID(as_uuid=True), primary_key=True)
    path = Column(Text, unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    hashes = relationship("PhotoHashesORM", back_populates="photo", uselist=False, cascade="all, delete-orphan")
    tags = relationship("PhotoTagORM", back_populates="photo", cascade="all, delete-orphan")


class PhotoHashesORM(Base):
    __tablename__ = "photo_hashes"

    photo_id = Column(UUID(as_uuid=True), ForeignKey("photos.id", ondelete="CASCADE"), primary_key=True)
    phash = Column(Text)
    ahash = Column(Text)
    dhash = Column(Text)

    photo = relationship("PhotoORM", back_populates="hashes")


class PhotoTagORM(Base):
    __tablename__ = "photo_tags"

    photo_id = Column(UUID(as_uuid=True), ForeignKey("photos.id", ondelete="CASCADE"), primary_key=True)
    tag = Column(Text, primary_key=True)

    photo = relationship("PhotoORM", back_populates="tags")
