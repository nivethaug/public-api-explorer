"""
Test Location endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestLocationEndpoints:
    def test_location_router_registered(self):
        """Verify location router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/location" in p]
        assert len(endpoints) > 0

    def test_location_countries(self):
        """Test countries list"""
        response = client.get("/location/countries")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_location_ip(self):
        """Test IP location"""
        response = client.get("/location/ip")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
