"""ProcessTime middleware."""

import time
from collections.abc import Callable

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp


class ProcessTimeMiddleware(BaseHTTPMiddleware):
    """
    Middleware to add the process time in the response header for each request.
    """

    def __init__(self, app: ASGIApp) -> None:
        """Initialize the middleware."""
        super().__init__(app)

    async def dispatch(
        self, request: Request, call_next: Callable[..., Request]
    ) -> Response:
        """
        Parameters
        ----------
        request : Request
            The request object
        call_next : Callable
            The next middleware in the chain

        Returns
        -------
        Response
            The response object
        """

        start_time = time.time()
        response: Response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["Process-Time"] = str(f"{process_time:0.4f} sec")

        return response
