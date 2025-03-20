"""Health Endpoint Test"""

import pytest
from fastapi.testclient import TestClient

from app.core.config import settings
from app.tests.order import get_pyorder


@pytest.mark.order(get_pyorder("health"))
def test_health(client: TestClient) -> None:
    """Test Health Endpoint"""
    response = client.get(f"{settings.API_V1_STR}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
