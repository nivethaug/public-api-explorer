"""
Security & Validation Routes
Documentation for security and threat intelligence public APIs

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/security", tags=["Security"])
http_client = get_http_client()


# ==================== UK POLICE DATA ====================

@router.get("/police/forces",
            summary="Get UK police forces list")
async def get_police_forces():
    """
    Get list of UK police forces
    
    **Real API URL:** `https://data.police.uk/api/forces`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://data.police.uk/api/forces')
    forces = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://data.police.uk/api/forces"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "UK Police Data"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"UK Police API error: {str(e)}")


@router.get("/police/crimes",
            summary="Get crime statistics by location")
async def get_crimes_by_location(
    lat: float = Query(..., ge=-90, le=90, description="Latitude"),
    lng: float = Query(..., ge=-180, le=180, description="Longitude"),
    date: str = Query(None, description="Date in YYYY-MM format (e.g., '2023-01')")
):
    """
    Get crime statistics for a specific location
    
    **Real API URL:** `https://data.police.uk/api/crimes-at-location`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://data.police.uk/api/crimes-at-location',
        params={'lat': 51.5074, 'lng': -0.1278}
    )
    crimes = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://data.police.uk/api/crimes-at-location"
        params = {"lat": lat, "lng": lng}
        if date:
            params["date"] = date
            
        response = await http_client.get(real_url, params=params)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "UK Police Data"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"UK Police API error: {str(e)}")


# ==================== URLHAUS ====================

@router.get("/urlhaus/recent",
            summary="Get recent malicious URLs from URLhaus")
async def get_urlhaus_recent(
    limit: int = Query(10, ge=1, le=100, description="Number of results")
):
    """
    Get recent malicious URLs from URLhaus threat intelligence
    
    **Real API URL:** `https://urlhaus-api.abuse.ch/v1/urls/recent/`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly (POST request)
    response = requests.post('https://urlhaus-api.abuse.ch/v1/urls/recent/')
    urls = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://urlhaus-api.abuse.ch/v1/urls/recent/"
        # URLhaus uses POST for this endpoint
        response = await http_client.post(real_url)
        response.raise_for_status()
        
        data = response.json()
        if limit and "urls" in data:
            data["urls"] = data["urls"][:limit]
        
        return JSONResponse(
            content=data,
            headers={"x-api-url": real_url, "x-api-provider": "URLhaus"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"URLhaus API error: {str(e)}")


# ==================== NVD (National Vulnerability Database) ====================

@router.get("/nvd/cves",
            summary="Search CVE vulnerabilities from NVD")
async def search_cves(
    keyword: str = Query(None, description="Keyword search"),
    results_per_page: int = Query(10, ge=1, le=100, description="Results per page")
):
    """
    Search CVE vulnerabilities from National Vulnerability Database
    
    **Real API URL:** `https://services.nvd.nist.gov/rest/json/cves/2.0`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://services.nvd.nist.gov/rest/json/cves/2.0',
        params={'keywordSearch': 'log4j', 'resultsPerPage': 10}
    )
    cves = response.json()
    ```
    
    **Note:** NVD has rate limits - be patient with responses
    """
    try:
        real_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
        params = {"resultsPerPage": results_per_page}
        if keyword:
            params["keywordSearch"] = keyword
            
        response = await http_client.get(real_url, params=params)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "NVD"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"NVD API error: {str(e)}")


@router.get("/nvd/cves/{cve_id}",
            summary="Get specific CVE details")
async def get_cve_details(
    cve_id: str = Path(..., description="CVE ID (e.g., 'CVE-2021-44228')")
):
    """
    Get details for a specific CVE vulnerability
    
    **Real API URL:** `https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://services.nvd.nist.gov/rest/json/cves/2.0',
        params={'cveId': 'CVE-2021-44228'}
    )
    cve = response.json()
    ```
    
    **Note:** NVD has rate limits - be patient with responses
    """
    try:
        real_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
        response = await http_client.get(
            real_url,
            params={"cveId": cve_id.upper()}
        )
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": f"{real_url}?cveId={cve_id}", "x-api-provider": "NVD"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"NVD API error: {str(e)}")
