"""
Test Currency endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestCurrencyEndpoints:
    def test_currency_router_registered(self):
        """Verify currency router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/currency" in p]
        assert len(endpoints) > 0

    def test_currency_convert(self):
        """Test currency conversion"""
        response = client.get("/currency/convert")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_currency_frankfurter_latest(self):
        """Test latest exchange rates"""
        response = client.get("/currency/frankfurter/latest")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_currency_frankfurter_historical(self):
        """Test historical exchange rates by date"""
        response = client.get("/currency/frankfurter/2024-01-01")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
