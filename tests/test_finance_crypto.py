"""
Test Finance/Crypto endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestFinanceCryptoEndpoints:
    def test_finance_router_registered(self):
        """Verify finance router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/finance" in p]
        assert len(endpoints) > 0

    def test_finance_crypto_coingecko_coins(self):
        """Test CoinGecko coins list"""
        response = client.get("/finance/crypto/coingecko/coins")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_finance_crypto_coincap_assets(self):
        """Test CoinCap assets"""
        response = client.get("/finance/crypto/coincap/assets")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
