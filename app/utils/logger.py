"""Logging utilities"""

import logging

import uvicorn

FORMAT = "%(levelprefix)s %(asctime)s | %(message)s"


def configure_logging() -> logging.Logger:
    """
    Creates a root logger with a `StreamHandler` that has level and formatting
    set from `config`.

    Returns:
        logging.Logger
    """
    logger = logging.getLogger("api")
    handler = logging.StreamHandler()
    formatter = uvicorn.logging.DefaultFormatter(FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


logger = configure_logging()


def get_logger(name: str | None = None) -> logging.Logger:
    """
    Returns a logger.

    Args:
        - name (str): if `None`, the root logger is returned. If provided, a child
            logger of the name `"api.{name}"` is returned. The child logger inherits
            the root logger's settings.

    Returns:
        logging.Logger
    """
    if name is None:
        return logger
    else:
        return logger.getChild(name)


def log_exception(
    exc: str,
    logger: logging.Logger = get_logger(),
) -> None:
    """Logs an exception"""
    logger.error(exc)
