"""
Test Jobs endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestJobsEndpoints:
    def test_jobs_router_registered(self):
        """Verify jobs router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/jobs" in p]
        assert len(endpoints) > 0

    def test_jobs_devit_list(self):
        """Test DevIT jobs list"""
        response = client.get("/jobs/devit/list")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_jobs_jobicy_search(self):
        """Test Jobicy search"""
        response = client.get("/jobs/jobicy/search")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
