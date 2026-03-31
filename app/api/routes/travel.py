"""
Travel Routes
Documentation for travel and places public APIs

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/travel", tags=["Travel"])
http_client = get_http_client()


# ==================== REST COUNTRIES (Extended) ====================

@router.get("/capital/{country}",
            summary="Get capital city by country")
async def get_capital_by_country(
    country: str = Path(..., description="Country name")
):
    """
    Get capital city information
    
    **Real API URL:** `https://restcountries.com/v3.1/capital/{capital}`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(f'https://restcountries.com/v3.1/name/{country}')
    data = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = f"https://restcountries.com/v3.1/name/{country}"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "REST Countries"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"REST Countries API error: {str(e)}")


# ==================== OPEN TRIP MAP ====================

@router.get("/opentripmap/places",
            summary="Search places on OpenTripMap")
async def search_opentripmap_places(
    query: str = Query(..., description="Search query"),
    radius: int = Query(1000, ge=100, le=50000, description="Search radius in meters")
):
    """
    Search for places using OpenTripMap
    
    **Real API URL:** `https://api.opentripmap.com/places/geoname`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://api.opentripmap.com/places/geoname',
        params={'name': 'Paris', 'radius': 1000}
    )
    places = response.json()
    ```
    
    **Note:** Free tier has rate limits
    """
    try:
        real_url = "https://api.opentripmap.com/places/geoname"
        response = await http_client.get(
            real_url,
            params={
                "name": query,
                "radius": radius,
                "apikey": "5ae69e5e3m0d99438b0e5d7e5e5e5e5e5e5e5e5"  # Demo key
            }
        )
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "OpenTripMap"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenTripMap API error: {str(e)}")


# ==================== TIME ZONE ====================

@router.get("/timezone/{lat},{lon}",
            summary="Get timezone by coordinates")
async def get_timezone_by_coords(
    lat: float = Path(..., ge=-90, le=90, description="Latitude"),
    lon: float = Path(..., ge=-180, le=180, description="Longitude")
):
    """
    Get timezone information for coordinates
    
    **Real API URL:** `https://timezoneapi.io/api/timezone`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        f'https://timezoneapi.io/api/timezone?lat={lat}&lon={lon}'
    )
    timezone = response.json()
    ```
    
    **Note:** Free tier available
    """
    try:
        real_url = f"https://timezoneapi.io/api/timezone?lat={lat}&lon={lon}"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "TimezoneAPI"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Timezone API error: {str(e)}")
