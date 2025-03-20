"""Logger Middleware."""

import logging

from starlette.requests import Request
from starlette.types import ASGIApp, Receive, Scope, Send

from app.utils.logger import get_logger

logger = get_logger(__name__)


class LoggerMiddleware:
    """MiddleWare to add logging."""

    def __init__(
        self,
        app: ASGIApp,
        querystrings: bool = False,
        headers: bool = False,
    ) -> None:
        """Init Middleware.

        Parameters:
        -----------
            app (ASGIApp): starlette/FastAPI application.

        """
        self.app = app
        self.querystrings = querystrings
        self.headers = headers
        self.logger = logger
        logger.setLevel(logging.DEBUG)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """Handle call."""
        if scope["type"] == "http":
            request = Request(scope)

            self.logger.debug(str(request.url))

            qs = dict(request.query_params)

            if qs and self.querystrings:
                self.logger.debug(qs)

            if self.headers:
                self.logger.debug(dict(request.headers))

        await self.app(scope, receive, send)
