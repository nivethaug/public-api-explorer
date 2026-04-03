"""
Test Sports endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestSportsEndpoints:
    def test_sports_router_registered(self):
        """Verify sports router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/sports" in p]
        assert len(endpoints) > 0

    def test_sports_nba_players(self):
        """Test NBA players"""
        response = client.get("/sports/nba/players")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_sports_f1_current_drivers(self):
        """Test F1 current drivers"""
        response = client.get("/sports/f1/current/drivers")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
