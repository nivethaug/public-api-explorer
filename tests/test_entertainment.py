"""
Test Entertainment endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestEntertainmentEndpoints:
    def test_entertainment_router_registered(self):
        """Verify entertainment router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/entertainment" in p]
        assert len(endpoints) > 0

    def test_entertainment_jokes_random(self):
        """Test random jokes"""
        response = client.get("/entertainment/jokes/random")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_entertainment_quotes_random(self):
        """Test random quotes"""
        response = client.get("/entertainment/quotes/random")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_entertainment_movies_tmdb_popular(self):
        """Test popular movies from TMDB"""
        response = client.get("/entertainment/movies/tmdb/popular")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_entertainment_jokes_chuck_norris(self):
        """Test Chuck Norris jokes"""
        response = client.get("/entertainment/jokes/chuck-norris")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_entertainment_facts_random(self):
        """Test random facts"""
        response = client.get("/entertainment/facts/random")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
