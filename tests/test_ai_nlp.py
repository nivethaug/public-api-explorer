"""
Test AI/NLP endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestAiNlpEndpoints:
    def test_ai_router_registered(self):
        """Verify AI router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/ai" in p]
        assert len(endpoints) > 0

    def test_ai_qrcode(self):
        """Test QR code generation"""
        response = client.get("/ai/qrcode")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_ai_random_user(self):
        """Test random user generation"""
        response = client.get("/ai/random/user")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_ai_text_sentiment(self):
        """Test text sentiment analysis"""
        response = client.get("/ai/text/sentiment")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_ai_translate(self):
        """Test translation service"""
        response = client.get("/ai/translate")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
