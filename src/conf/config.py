from pydantic_settings import BaseSettings
from pydantic import EmailStr, ConfigDict
import os
from dotenv import load_dotenv
from typing import Optional


# Load environment variables from the .env file
load_dotenv()


class Settings(BaseSettings):
    # Database settings
    DB_URL: str = "postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # jwt
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    ALGORITHM: str = "HS256"
    SECRET_KEY: str = "secret"

    # redis
    REDIS_URL: str = "redis://localhost"

    # mail
    MAIL_USERNAME: EmailStr = "example@meta.ua"
    MAIL_PASSWORD: str = "secretPassword"
    MAIL_FROM: EmailStr = "example@meta.ua"
    MAIL_PORT: int = 465
    MAIL_SERVER: str = "smtp.meta.ua"
    MAIL_FROM_NAME: str = "Rest API Service"
    MAIL_STARTTLS: bool = False
    MAIL_SSL_TLS: bool = True
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True

    # cloudinary
    CLD_NAME: Optional[str] = None
    CLD_API_KEY: int = 326488457974591
    CLD_API_SECRET: str = "secret"

    model_config = ConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True, extra="ignore"
    )

    # Post-processing for DB_URL to ensure that environment variables are replaced properly
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.DB_URL = self.DB_URL.format(
            POSTGRES_USER=os.getenv("POSTGRES_USER"),
            POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD"),
            POSTGRES_HOST=os.getenv("POSTGRES_HOST"),
            POSTGRES_PORT=os.getenv("POSTGRES_PORT"),
            POSTGRES_DB=os.getenv("POSTGRES_DB")
        )


# Create the settings object
settings = Settings()
