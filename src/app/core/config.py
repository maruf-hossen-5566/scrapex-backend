from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    APP_NAME: str = "Scrapex"
    DEBUG: bool = False
    PROXY_SERVER: str
    PROXY_USERNAME: str
    PROXY_PASSWORD: str
    BRIGHT_DATA_API: str

    class Config:
        env_file = BASE_DIR / ".env"


settings = Settings()  # type: ignore
