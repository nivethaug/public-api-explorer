"""
Maps & Location Routes
Documentation for geocoding, IP location, and country public APIs

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/location", tags=["Maps & Location"])
http_client = get_http_client()


@router.get("/countries",
            summary="List all countries")
async def get_all_countries(
    name: str = Query(None, description="Filter by country name"),
    region: str = Query(None, description="Filter by region (e.g., Europe, Asia)")
):
    """
    Get list of all countries from REST Countries API
    
    **Real API URL:** `https://restcountries.com/v3.1/all`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    # Get all countries
    response = requests.get('https://restcountries.com/v3.1/all')
    
    # Search by name
    response = requests.get('https://restcountries.com/v3.1/name/united')
    
    # Filter by region
    response = requests.get('https://restcountries.com/v3.1/region/europe')
    
    data = response.json()
    ```
    
    **No authentication required**
    """
    try:
        if name:
            real_url = f"https://restcountries.com/v3.1/name/{name}"
        elif region:
            real_url = f"https://restcountries.com/v3.1/region/{region}"
        else:
            real_url = "https://restcountries.com/v3.1/all"
        
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "REST Countries"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"REST Countries API error: {str(e)}")


@router.get("/countries/{code}",
            summary="Get country by code")
async def get_country_by_code(
    code: str = Path(..., min_length=2, max_length=3, description="Country code (ISO 3166-1)")
):
    """Get country information by country code"""
    try:
        response = await http_client.get(
            f"https://restcountries.com/v3.1/alpha/{code}"
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"REST Countries API error: {str(e)}")


@router.get("/geocode",
            summary="Reverse geocoding")
async def reverse_geocode(
    lat: float = Query(..., ge=-90, le=90, description="Latitude"),
    lon: float = Query(..., ge=-180, le=180, description="Longitude")
):
    """Get address from coordinates using Nominatim (OpenStreetMap)"""
    try:
        response = await http_client.get(
            "https://nominatim.openstreetmap.org/reverse",
            params={
                "lat": lat,
                "lon": lon,
                "format": "json"
            },
            headers={"User-Agent": "PublicAPIExplorer/1.0"}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Nominatim API error: {str(e)}")


@router.get("/ip",
            summary="Get IP geolocation")
async def get_ip_location(
    ip: str = Query(None, description="IP address (uses your IP if not provided)")
):
    """Get geolocation data for an IP address"""
    try:
        url = "http://ip-api.com/json/"
        if ip:
            url += ip
        
        response = await http_client.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"IP API error: {str(e)}")


@router.get("/ipify",
            summary="Get your public IP address")
async def get_public_ip():
    """Get your current public IP address using IPify"""
    try:
        response = await http_client.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"IPify API error: {str(e)}")