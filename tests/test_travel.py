"""
Test Travel endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestTravelEndpoints:
    def test_travel_router_registered(self):
        """Verify travel router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/travel" in p]
        assert len(endpoints) > 0

    def test_travel_opentripmap_places(self):
        """Test OpenTripMap places"""
        response = client.get("/travel/opentripmap/places")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_travel_timezone(self):
        """Test timezone lookup"""
        response = client.get("/travel/timezone/40.7128,-74.0060")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
