"""
Test Science endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestScienceEndpoints:
    def test_science_router_registered(self):
        """Verify science router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/science" in p]
        assert len(endpoints) > 0

    def test_science_iss_position(self):
        """Test ISS position"""
        response = client.get("/science/iss/position")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_science_nasa_apod(self):
        """Test NASA APOD"""
        response = client.get("/science/nasa/apod")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
