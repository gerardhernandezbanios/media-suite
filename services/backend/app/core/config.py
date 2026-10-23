#services/backend/app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str = "dev"
    DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost:5432/media"

    WORK_BASE_PATH: str = "/data/work"
    MEDIA_ROOT: str = "/data/media"

    class Config:
        env_file = ".env"

settings = Settings()
