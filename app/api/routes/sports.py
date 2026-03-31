"""
Sports Routes
Documentation for sports scores and statistics public APIs

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/sports", tags=["Sports"])
http_client = get_http_client()


# ==================== FOOTBALL ====================

@router.get("/football/matches",
            summary="Get football matches")
async def get_football_matches():
    """
    Get football/soccer matches from football-data.org
    
    **Real API URL:** `https://api.football-data.org/v4/matches`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    API_KEY = 'your_football_data_api_key'
    response = requests.get(
        'https://api.football-data.org/v4/matches',
        headers={'X-Auth-Token': API_KEY}
    )
    matches = response.json()
    ```
    
    **Note:** Requires free API key from football-data.org
    """
    try:
        real_url = "https://api.football-data.org/v4/matches"
        return JSONResponse(
            content={
                "message": "Football-data.org API requires authentication",
                "real_url": real_url,
                "how_to_use": {
                    "step1": "Get free API key from http://api.football-data.org/client/register",
                    "step2": f"Call: {real_url} with header 'X-Auth-Token: YOUR_KEY'",
                    "example": f"requests.get('{real_url}', headers={{'X-Auth-Token': 'YOUR_KEY'}})"
                }
            },
            headers={"x-api-url": real_url, "x-api-provider": "Football-Data.org"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Football API error: {str(e)}")


# ==================== NBA ====================

@router.get("/nba/players",
            summary="Get NBA players")
async def get_nba_players():
    """
    Get NBA players data
    
    **Real API URL:** `https://www.balldontlie.io/api/v1/players`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://www.balldontlie.io/api/v1/players')
    players = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://www.balldontlie.io/api/v1/players"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Ball Don't Lie"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"NBA API error: {str(e)}")


@router.get("/nba/teams",
            summary="Get NBA teams")
async def get_nba_teams():
    """
    Get NBA teams data
    
    **Real API URL:** `https://www.balldontlie.io/api/v1/teams`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://www.balldontlie.io/api/v1/teams')
    teams = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://www.balldontlie.io/api/v1/teams"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Ball Don't Lie"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"NBA API error: {str(e)}")


# ==================== FORMULA 1 ====================

@router.get("/f1/current/drivers",
            summary="Get current F1 drivers")
async def get_f1_drivers():
    """
    Get current Formula 1 drivers
    
    **Real API URL:** `https://ergast.com/api/f1/current/drivers.json`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://ergast.com/api/f1/current/drivers.json')
    drivers = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://ergast.com/api/f1/current/drivers.json"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Ergast F1"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"F1 API error: {str(e)}")
