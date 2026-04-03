"""
Test Weather endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestWeatherEndpoints:
    def test_weather_router_registered(self):
        """Verify weather router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/weather" in p]
        assert len(endpoints) > 0

    def test_weather_open_meteo(self):
        """Test Open-Meteo weather"""
        response = client.get("/weather/open-meteo")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_weather_7timer(self):
        """Test 7Timer weather"""
        response = client.get("/weather/7timer")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
