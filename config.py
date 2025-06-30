from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str = "sqlite:///./tasks.db"
    
    # API settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DEBUG: bool = True
    
    # Application information
    APP_TITLE: str = "Task Management API"
    APP_DESCRIPTION: Optional[str] = "A FastAPI-based REST API for managing tasks"
    APP_VERSION: str = "0.1.0"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """
    Returns cached settings to avoid loading .env file on each request
    """
    return Settings()
