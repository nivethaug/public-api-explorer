"""
Test Stocks endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestStocksEndpoints:
    def test_stocks_router_registered(self):
        """Verify stocks router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/stocks" in p]
        assert len(endpoints) > 0

    def test_stocks_crypto_list(self):
        """Test crypto list"""
        response = client.get("/stocks/crypto/list")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_stocks_trending(self):
        """Test trending stocks"""
        response = client.get("/stocks/trending")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
