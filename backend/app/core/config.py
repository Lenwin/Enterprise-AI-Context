from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --------------------
    # Application
    # --------------------
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    # --------------------
    # API
    # --------------------
    API_V1_PREFIX: str

    # --------------------
    # Security
    # --------------------
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # --------------------
    # Database
    # --------------------
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()