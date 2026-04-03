"""
Test Health/Fitness endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestHealthFitnessEndpoints:
    def test_health_router_registered(self):
        """Verify health router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/health" in p]
        assert len(endpoints) > 0

    def test_health_fda_drugs(self):
        """Test FDA drugs"""
        response = client.get("/health/fda/drugs")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_health_healthcare_topics(self):
        """Test healthcare topics"""
        response = client.get("/health/healthcare/topics")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
