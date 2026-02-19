import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str
    db_url: str

    class Config:
        # Solo cargamos .env si existe (modo desarrollo)
        env_file = (
            os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
            if os.path.exists(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))
            else None
        )
        env_file_encoding = "utf-8"

settings = Settings()
