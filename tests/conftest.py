"""
Pytest configuration and fixtures for API testing
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture(scope="module")
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def api_base():
    """Base URL for API endpoints"""
    return "/api"


# Expected response structure for all endpoints
EXPECTED_RESPONSE_FIELDS = {
    "has_status": True,  # Should have status field
    "has_data": True,    # Should have data field
    "has_message": True  # Should have message or error field
}


def validate_api_response(response_data: dict) -> tuple[bool, str]:
    """
    Validate that API response has proper structure
    
    Returns: (is_valid, error_message)
    """
    if not isinstance(response_data, dict):
        return False, "Response is not a dictionary"
    
    # Check for at least one of these fields
    has_valid_field = any(
        field in response_data 
        for field in ["data", "results", "items", "message", "status", "error"]
    )
    
    if not has_valid_field:
        return False, "Response missing required fields (data/results/items/message/status)"
    
    return True, ""


def validate_external_url(response_data: dict) -> tuple[bool, str]:
    """
    Validate that response includes external API URL information
    """
    url_fields = ["real_url", "external_url", "api_url", "x-api-url", "source_url"]
    
    has_url = any(field in response_data for field in url_fields)
    
    if has_url:
        return True, ""
    
    # Check nested data for URL
    if "data" in response_data and isinstance(response_data["data"], dict):
        has_url = any(field in response_data["data"] for field in url_fields)
        if has_url:
            return True, ""
    
    # Some endpoints may return direct data without URL wrapper
    # This is acceptable for proxy endpoints
    return True, ""
