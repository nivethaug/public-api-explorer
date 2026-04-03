"""
Jobs & Career Routes
Documentation for job search public APIs

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/jobs", tags=["Jobs & Career"])
http_client = get_http_client()


# ==================== JOBICY ====================

@router.get("/jobicy/search",
            summary="Search jobs on Jobicy")
async def search_jobicy_jobs(
    query: str = Query(..., description="Search query (e.g., 'python', 'marketing')"),
    location: str = Query(None, description="Location filter (e.g., 'remote', 'new york')")
):
    """
    Search jobs on Jobicy platform
    
    **Real API URL:** `https://api.jobicy.com/v2/search`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://api.jobicy.com/v2/search',
        params={'query': 'python', 'location': 'remote'}
    )
    jobs = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://api.jobicy.com/v2/search"
        params = {"query": query}
        if location:
            params["location"] = location
            
        response = await http_client.get(real_url, params=params)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Jobicy"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Jobicy API error: {str(e)}")


@router.get("/jobicy/list",
            summary="List jobs by category on Jobicy")
async def list_jobicy_jobs(
    category: str = Query(None, description="Job category (e.g., 'developer', 'marketing', 'design')"),
    limit: int = Query(20, ge=1, le=100, description="Number of results")
):
    """
    List jobs from Jobicy by category
    
    **Real API URL:** `https://api.jobicy.com/v2/jobs`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://api.jobicy.com/v2/jobs',
        params={'category': 'developer', 'limit': 20}
    )
    jobs = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://api.jobicy.com/v2/jobs"
        params = {"limit": limit}
        if category:
            params["category"] = category
            
        response = await http_client.get(real_url, params=params)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Jobicy"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Jobicy API error: {str(e)}")


# ==================== DEVITJOBS ====================

@router.get("/devit/search",
            summary="Search IT jobs on DevITjobs")
async def search_devit_jobs(
    query: str = Query(..., description="Search query (e.g., 'react', 'devops')"),
    remote: bool = Query(None, description="Filter for remote jobs")
):
    """
    Search IT jobs on DevITjobs platform
    
    **Real API URL:** `https://devitjobs.com/api/jobs/search`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://devitjobs.com/api/jobs/search',
        params={'query': 'react', 'remote': True}
    )
    jobs = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://devitjobs.com/api/jobs/search"
        params = {"query": query}
        if remote is not None:
            params["remote"] = str(remote).lower()
            
        response = await http_client.get(real_url, params=params)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "DevITjobs"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DevITjobs API error: {str(e)}")


@router.get("/devit/list",
            summary="List IT jobs from DevITjobs")
async def list_devit_jobs(
    skill: str = Query(None, description="Filter by skill (e.g., 'python', 'javascript')"),
    limit: int = Query(20, ge=1, le=100, description="Number of results")
):
    """
    List IT jobs from DevITjobs
    
    **Real API URL:** `https://devitjobs.com/api/jobs`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://devitjobs.com/api/jobs',
        params={'skill': 'python', 'limit': 20}
    )
    jobs = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://devitjobs.com/api/jobs"
        params = {"limit": limit}
        if skill:
            params["skill"] = skill
            
        response = await http_client.get(real_url, params=params)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "DevITjobs"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DevITjobs API error: {str(e)}")
