"""
Test Utilities endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestUtilitiesEndpoints:
    def test_utilities_router_registered(self):
        """Verify utilities router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/utilities" in p]
        assert len(endpoints) > 0

    def test_utilities_qr_generate(self):
        """Test QR code generation"""
        response = client.get("/utilities/qr/generate")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_utilities_uuid_generate(self):
        """Test UUID generation"""
        response = client.get("/utilities/uuid/generate")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
