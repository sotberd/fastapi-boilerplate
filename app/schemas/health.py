"""Health schema."""

from pydantic import BaseModel


class HealthCheck(BaseModel):
    """Health check response schema."""

    status: str
