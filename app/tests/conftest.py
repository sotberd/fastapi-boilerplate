"""PyTest Conftest"""

from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, None, None]:
    """FastAPI client"""
    with TestClient(app) as c:
        yield c
