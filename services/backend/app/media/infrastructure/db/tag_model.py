# services/backend/app/media/infrastructure/db/tag_model.py

from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Enum, ForeignKey, Float, DateTime, Index
from app.media.domain.entities import MediaType

class Base(DeclarativeBase):
    pass
class TagModel(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
