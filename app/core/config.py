"""
Application Configuration
Centralized configuration settings for the Public API Explorer
"""

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings"""
    
    # App Info
    APP_NAME: str = "Public API Explorer"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "A comprehensive collection of 20 API categories with 100% no-auth APIs for Telegram bot developers"
    
    # Server Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    
    # CORS Settings
    CORS_ORIGINS: List[str] = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ["*"]
    CORS_ALLOW_HEADERS: List[str] = ["*"]
    
    # HTTP Client Settings
    HTTP_TIMEOUT: float = 30.0
    HTTP_MAX_RETRIES: int = 3
    
    # API Documentation
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()
