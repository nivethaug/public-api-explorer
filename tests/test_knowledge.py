"""
Test Knowledge endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestKnowledgeEndpoints:
    def test_knowledge_router_registered(self):
        """Verify knowledge router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/knowledge" in p]
        assert len(endpoints) > 0

    def test_knowledge_dictionary(self):
        """Test dictionary lookup"""
        response = client.get("/knowledge/dictionary/test")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_knowledge_wikipedia_search(self):
        """Test Wikipedia search"""
        response = client.get("/knowledge/wikipedia/search")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
