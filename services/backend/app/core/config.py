#services/backend/app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str = "dev"
    DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost:5432/media"

    MEDIA_ROOT: str = "/data/media"

    class Config:
        env_file = ".env"

settings = Settings()
