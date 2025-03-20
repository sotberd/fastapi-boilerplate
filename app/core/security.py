"""Security module for API Key authentication"""

from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette import status

from app.core.config import settings

schema_name = "API Key Authentication"
description = """
This API uses API Key authentication. To authenticate, add your API Key to the `X-API-KEY` header of your request.
"""

# Define the name of HTTP header to retrieve an API key from
api_key_header = APIKeyHeader(
    name=settings.API_KEY_NAME,
    scheme_name=schema_name,
    description=description,
    auto_error=False,
)


def get_api_key(
    api_key_header: str = Security(api_key_header),
):
    """Retrieve & validate an API key from the query parameters or HTTP header"""
    # If the API Key is not present in the header of the request & is valid, return it
    if api_key_header not in settings.API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
        )
