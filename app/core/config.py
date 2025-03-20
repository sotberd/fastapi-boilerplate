"""Application configuration."""

from typing import Annotated, Any

from pydantic import AnyUrl, BeforeValidator
from pydantic_settings import BaseSettings, SettingsConfigDict


def parse_cors(v: Any) -> list[str] | str:
    """Parse CORS origins."""
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    """Application settings."""

    # General settings
    DEBUG: bool = True

    APP_NAME: str = "FastAPI Boilerplate"
    API_V1_STR: str = "/api/v1"

    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/"
    OPENAPI_JSON_PATH: str = "./openapi.json"

    VERSION: str = "1.0.0"

    # Security settings

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost:4200", "http://local.dockertoolbox.imageryapi.com"]'
    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []
    API_KEY_NAME: str = "X-API-KEY"
    API_KEYS: list[str] = []

    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )


settings = Settings()
