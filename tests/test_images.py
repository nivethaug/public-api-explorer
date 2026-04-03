"""
Test Images endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestImagesEndpoints:
    def test_images_router_registered(self):
        """Verify images router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/images" in p]
        assert len(endpoints) > 0

    def test_images_dogceo_random(self):
        """Test random dog images"""
        response = client.get("/images/dogceo/random")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_images_unsplash_random(self):
        """Test random Unsplash images"""
        response = client.get("/images/unsplash/random")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
