"""Health API endpoint."""

from fastapi import APIRouter, status

from app.schemas.health import HealthCheck

router = APIRouter()


@router.get(
    "/health",
    summary="Health check the service",
    response_description="Status of the service",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def health_check() -> HealthCheck:
    """Responds with the status of the service."""
    return HealthCheck(status="OK")
