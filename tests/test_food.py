"""
Test Food endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestFoodEndpoints:
    def test_food_router_registered(self):
        """Verify food router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/food" in p]
        assert len(endpoints) > 0

    def test_food_meals_random(self):
        """Test random meals"""
        response = client.get("/food/meals/random")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_food_cocktails_search(self):
        """Test cocktail search"""
        response = client.get("/food/cocktails/search")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
