"""Application configuration."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # Home Assistant
    HA_URL: str = "http://homeassistant.local:8123"
    HA_TOKEN: str = ""

    # Server
    MCP_HOST: str = "0.0.0.0"
    MCP_PORT: int = 8000
    MCP_DEBUG: bool = False

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"

    # Notifications
    DEFAULT_NOTIFICATION_SOUND: str = "default"
    NOTIFICATION_TIMEOUT: int = 30

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
