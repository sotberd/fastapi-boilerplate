"""Exception Handlers."""

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException, RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

from .logger import log_exception


async def http_exception_handler(_: Request, exc: HTTPException) -> JSONResponse:
    """Handle HTTP exceptions."""
    log_exception(f"{exc.status_code}: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(
            {"error": f"{str(exc.detail)}", "status_code": exc.status_code}
        ),
    )


async def validation_exception_handler(
    _: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    """Handle validation exceptions."""
    responsible_value = exc.errors()[0]["loc"][-1]
    reason = exc.errors()[0]["msg"]

    error = f"({str(responsible_value)}) {str(reason)}"

    log_exception(f"{status.HTTP_422_UNPROCESSABLE_ENTITY}: {error}")

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            {
                "error": error,
                "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
            }
        ),
    )
