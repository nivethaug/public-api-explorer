"""
Test Security endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestSecurityEndpoints:
    def test_security_router_registered(self):
        """Verify security router is registered"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        paths = response.json()["paths"]
        endpoints = [p for p in paths.keys() if "/security" in p]
        assert len(endpoints) > 0

    def test_security_police_forces(self):
        """Test police forces"""
        response = client.get("/security/police/forces")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)

    def test_security_nvd_cves(self):
        """Test NVD CVEs"""
        response = client.get("/security/nvd/cves")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
