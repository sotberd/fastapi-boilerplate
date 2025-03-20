import json
from typing import Any

from fastapi import Depends, FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.api import docs, main
from app.core.config import settings
from app.core.security import get_api_key
from app.middleware.logger import LoggerMiddleware
from app.middleware.process_time import ProcessTimeMiddleware
from app.utils.exception_handlers import (
    http_exception_handler,
    validation_exception_handler,
)
from app.utils.logger import get_logger

logger = get_logger(__name__)


def custom_generate_unique_id(route: APIRoute) -> str:
    """Generate unique id for route"""
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title=settings.APP_NAME,
    docs_url=None if not settings.DOCS_URL else settings.DOCS_URL,
    redoc_url=None if not settings.REDOC_URL else settings.REDOC_URL,
    generate_unique_id_function=custom_generate_unique_id,
    dependencies=[Depends(get_api_key)] if settings.API_KEYS else [],
)

# Exception handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=(
        [str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS]
        if settings.BACKEND_CORS_ORIGINS
        else ["*"]
    ),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if settings.DEBUG:
    app.add_middleware(LoggerMiddleware, headers=True, querystrings=True)
    app.add_middleware(ProcessTimeMiddleware)

app.include_router(main.api_router, prefix=settings.API_V1_STR)


def app_openapi() -> Any:  # pragma: no cover
    """Generate OpenAPI schema."""
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema: dict[str, Any] = get_openapi(
        title=settings.APP_NAME,
        version=settings.VERSION,
        routes=app.routes,
        summary=docs.summary,
        description=docs.description,
        tags=docs.tags_metadata,
    )
    with open(settings.OPENAPI_JSON_PATH) as openapi:
        openapi_data = json.load(openapi)
        contact = openapi_data["info"]["contact"]
        licence = openapi_data["info"]["license"]
        logo = openapi_data["info"]["x-logo"]
    openapi_schema["info"]["contact"] = contact
    openapi_schema["info"]["license"] = licence
    openapi_schema["info"]["x-logo"] = logo
    for components in docs.components_schemas:
        openapi_schema["components"]["schemas"][components["component"]] = components[
            "schema"
        ]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = app_openapi
