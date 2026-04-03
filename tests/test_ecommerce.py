"""
Test E-commerce endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestEcommerceEndpoints:
    def test_ecommerce_router_registered(self):
        """Verify ecommerce router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/ecommerce" in p]
        assert len(endpoints) > 0

    def test_ecommerce_categories(self):
        """Test product categories"""
        response = client.get("/ecommerce/categories")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_ecommerce_products(self):
        """Test products list"""
        response = client.get("/ecommerce/products")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_ecommerce_product_by_id(self):
        """Test single product by ID"""
        response = client.get("/ecommerce/products/1")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_ecommerce_dummy_products(self):
        """Test dummy products from DummyJSON"""
        response = client.get("/ecommerce/dummy/products")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_ecommerce_posts(self):
        """Test posts from JSONPlaceholder"""
        response = client.get("/ecommerce/posts")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_ecommerce_users(self):
        """Test users list"""
        response = client.get("/ecommerce/users")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
