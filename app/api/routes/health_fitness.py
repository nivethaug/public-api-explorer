"""
Health & Fitness Routes
Documentation for health and fitness public APIs

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/health", tags=["Health & Fitness"])
http_client = get_http_client()


# ==================== OPEN FDA ====================

@router.get("/fda/drugs",
            summary="Search FDA drug information")
async def search_fda_drugs(
    query: str = Query(..., description="Search query (e.g., 'aspirin', 'ibuprofen')"),
    limit: int = Query(10, ge=1, le=100, description="Number of results")
):
    """
    Search FDA drug label information
    
    **Real API URL:** `https://api.fda.gov/drug/label.json`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://api.fda.gov/drug/label.json',
        params={'search': 'aspirin', 'limit': 10}
    )
    drugs = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://api.fda.gov/drug/label.json"
        response = await http_client.get(
            real_url,
            params={"search": query, "limit": limit}
        )
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Open FDA"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"FDA API error: {str(e)}")


@router.get("/fda/food-recalls",
            summary="Get FDA food recalls")
async def get_fda_food_recalls(
    status: str = Query(None, description="Filter by status (e.g., 'ongoing')"),
    limit: int = Query(10, ge=1, le=100, description="Number of results")
):
    """
    Get FDA food enforcement and recall data
    
    **Real API URL:** `https://api.fda.gov/food/enforcement.json`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://api.fda.gov/food/enforcement.json',
        params={'limit': 10}
    )
    recalls = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://api.fda.gov/food/enforcement.json"
        params = {"limit": limit}
        if status:
            params["search"] = f"status:{status}"
            
        response = await http_client.get(real_url, params=params)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Open FDA"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"FDA API error: {str(e)}")


# ==================== HEALTHCARE.GOV ====================

@router.get("/healthcare/topics",
            summary="Get healthcare topics from Healthcare.gov")
async def get_healthcare_topics(
    language: str = Query("en", description="Language code (e.g., 'en', 'es')")
):
    """
    Get healthcare topics and information from Healthcare.gov
    
    **Real API URL:** `https://api.healthcare.gov/api/v1/topics`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://api.healthcare.gov/api/v1/topics',
        params={'lang': 'en'}
    )
    topics = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://api.healthcare.gov/api/v1/topics"
        response = await http_client.get(
            real_url,
            params={"lang": language}
        )
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Healthcare.gov"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Healthcare.gov API error: {str(e)}")
