"""
Science & Space Routes
Documentation for science and space public APIs

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/science", tags=["Science & Space"])
http_client = get_http_client()


# ==================== ISS (International Space Station) ====================

@router.get("/iss/position",
            summary="Get current ISS position")
async def get_iss_position():
    """
    Get the current position of the International Space Station
    
    **Real API URL:** `http://api.open-notify.org/iss-now.json`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('http://api.open-notify.org/iss-now.json')
    position = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "http://api.open-notify.org/iss-now.json"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Open Notify"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ISS API error: {str(e)}")


@router.get("/iss/crew",
            summary="Get current ISS crew members")
async def get_iss_crew():
    """
    Get the list of people currently in space (ISS crew)
    
    **Real API URL:** `http://api.open-notify.org/astros.json`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('http://api.open-notify.org/astros.json')
    crew = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "http://api.open-notify.org/astros.json"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Open Notify"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ISS API error: {str(e)}")


# ==================== SPACEX ====================

@router.get("/spacex/launches",
            summary="Get SpaceX launches")
async def get_spacex_launches(
    limit: int = Query(10, ge=1, le=100, description="Number of results")
):
    """
    Get SpaceX launch data
    
    **Real API URL:** `https://api.spacexdata.com/v4/launches`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://api.spacexdata.com/v4/launches')
    launches = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://api.spacexdata.com/v4/launches"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        data = response.json()
        if limit:
            data = data[:limit]
        
        return JSONResponse(
            content=data,
            headers={"x-api-url": real_url, "x-api-provider": "SpaceX API"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"SpaceX API error: {str(e)}")


@router.get("/spacex/rockets",
            summary="Get SpaceX rockets information")
async def get_spacex_rockets():
    """
    Get information about SpaceX rockets
    
    **Real API URL:** `https://api.spacexdata.com/v4/rockets`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://api.spacexdata.com/v4/rockets')
    rockets = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://api.spacexdata.com/v4/rockets"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "SpaceX API"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"SpaceX API error: {str(e)}")


# ==================== NASA ====================

@router.get("/nasa/apod",
            summary="Get NASA Astronomy Picture of the Day")
async def get_nasa_apod(
    date: str = Query(None, description="Date in YYYY-MM-DD format")
):
    """
    Get NASA's Astronomy Picture of the Day
    
    **Real API URL:** `https://api.nasa.gov/planetary/apod`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly (use DEMO_KEY for testing)
    response = requests.get(
        'https://api.nasa.gov/planetary/apod',
        params={'api_key': 'DEMO_KEY'}
    )
    apod = response.json()
    ```
    
    **Note:** Uses NASA DEMO_KEY for demo purposes
    """
    try:
        real_url = "https://api.nasa.gov/planetary/apod"
        params = {"api_key": "DEMO_KEY"}
        if date:
            params["date"] = date
            
        response = await http_client.get(real_url, params=params)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "NASA"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"NASA API error: {str(e)}")


@router.get("/nasa/mars/photos",
            summary="Get Mars rover photos")
async def get_mars_photos(
    rover: str = Query("curiosity", description="Rover name (curiosity, opportunity, spirit)"),
    sol: int = Query(1000, ge=0, description="Martian sol (day) number")
):
    """
    Get photos from Mars rovers
    
    **Real API URL:** `https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly (use DEMO_KEY for testing)
    response = requests.get(
        'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos',
        params={'sol': 1000, 'api_key': 'DEMO_KEY'}
    )
    photos = response.json()
    ```
    
    **Note:** Uses NASA DEMO_KEY for demo purposes
    """
    try:
        real_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos"
        params = {"sol": sol, "api_key": "DEMO_KEY"}
            
        response = await http_client.get(real_url, params=params)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "NASA"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"NASA API error: {str(e)}")


# ==================== USGS EARTHQUAKES ====================

@router.get("/earthquakes",
            summary="Get recent earthquake data from USGS")
async def get_earthquakes(
    min_magnitude: float = Query(4.5, ge=0, le=10, description="Minimum magnitude"),
    timeframe: str = Query("day", description="Timeframe: hour, day, week, month")
):
    """
    Get recent earthquake data from USGS
    
    **Real API URL:** `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{magnitude}_{timeframe}.geojson`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson'
    )
    earthquakes = response.json()
    ```
    
    **No authentication required**
    """
    try:
        # Map min_magnitude to USGS format
        magnitude_map = {0: "all", 1: "1.0", 2.5: "2.5", 4.5: "4.5", 5: "significant"}
        mag_key = min(magnitude_map.keys(), key=lambda x: abs(x - min_magnitude))
        mag_str = magnitude_map[mag_key]
        
        # Validate timeframe
        valid_timeframes = ["hour", "day", "week", "month"]
        if timeframe not in valid_timeframes:
            timeframe = "day"
        
        real_url = f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{mag_str}_{timeframe}.geojson"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "USGS"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"USGS API error: {str(e)}")