"""
Weather Routes
Documentation for weather public APIs

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/weather", tags=["Weather"])
http_client = get_http_client()


@router.get("/open-meteo",
            summary="Get current weather from Open-Meteo")
async def get_open_meteo_weather(
    latitude: float = Query(..., ge=-90, le=90, description="Latitude"),
    longitude: float = Query(..., ge=-180, le=180, description="Longitude")
):
    """
    Get current weather data from Open-Meteo
    
    **Real API URL:** `https://api.open-meteo.com/v1/forecast`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://api.open-meteo.com/v1/forecast',
        params={'latitude': 40.71, 'longitude': -74.01, 'current_weather': True}
    )
    data = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://api.open-meteo.com/v1/forecast"
        response = await http_client.get(
            real_url,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current_weather": "true",
                "hourly": "temperature_2m,relativehumidity_2m,windspeed_10m"
            }
        )
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Open-Meteo"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Open-Meteo API error: {str(e)}")


@router.get("/7timer",
            summary="Get weather forecast from 7Timer!")
async def get_7timer_forecast(
    lat: float = Query(..., ge=-90, le=90, description="Latitude"),
    lon: float = Query(..., ge=-180, le=180, description="Longitude"),
    product: str = Query("civillight", description="Product type (civil, civillight, meteo)")
):
    """Get weather forecast from 7Timer!"""
    try:
        response = await http_client.get(
            "http://www.7timer.info/bin/api.pl",
            params={
                "lat": round(lat, 1),
                "lon": round(lon, 1),
                "product": product,
                "output": "json"
            }
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"7Timer API error: {str(e)}")


@router.get("/nws/alerts",
            summary="Get US National Weather Service alerts")
async def get_nws_alerts(
    state: str = Query(None, min_length=2, max_length=2, description="US state code (e.g., CA, NY)")
):
    """Get weather alerts from US National Weather Service"""
    try:
        if state:
            url = f"https://api.weather.gov/alerts/active/area/{state.upper()}"
        else:
            url = "https://api.weather.gov/alerts/active"
        
        response = await http_client.get(
            url,
            headers={"User-Agent": "PublicAPIExplorer/1.0"}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"NWS API error: {str(e)}")
