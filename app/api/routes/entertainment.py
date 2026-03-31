"""
Entertainment Routes
Documentation for movies, music, and entertainment public APIs

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/entertainment", tags=["Entertainment"])
http_client = get_http_client()


# ==================== MOVIES ====================

@router.get("/movies/tmdb/popular",
            summary="Get popular movies from TMDB")
async def get_tmdb_popular_movies(
    page: int = Query(1, ge=1, description="Page number")
):
    """
    Get popular movies from The Movie Database
    
    **Real API URL:** `https://api.themoviedb.org/3/movie/popular`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    API_KEY = 'your_tmdb_api_key'
    response = requests.get(
        'https://api.themoviedb.org/3/movie/popular',
        params={'api_key': API_KEY, 'page': 1}
    )
    data = response.json()
    ```
    
    **Note:** Requires free TMDB API key
    """
    try:
        # Note: TMDB requires API key, showing structure
        real_url = "https://api.themoviedb.org/3/movie/popular"
        return JSONResponse(
            content={
                "message": "TMDB API requires authentication",
                "real_url": real_url,
                "how_to_use": {
                    "step1": "Get free API key from https://www.themoviedb.org/settings/api",
                    "step2": f"Call: {real_url}?api_key=YOUR_KEY&page={page}",
                    "example": f"requests.get('{real_url}', params={{'api_key': 'YOUR_KEY', 'page': {page}}})"
                }
            },
            headers={"x-api-url": real_url, "x-api-provider": "TMDB"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TMDB API error: {str(e)}")


# ==================== JOKES ====================

@router.get("/jokes/random",
            summary="Get random joke")
async def get_random_joke():
    """
    Get a random joke from JokeAPI
    
    **Real API URL:** `https://v2.jokeapi.dev/joke/Any`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://v2.jokeapi.dev/joke/Any')
    joke = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://v2.jokeapi.dev/joke/Any"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "JokeAPI"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"JokeAPI error: {str(e)}")


@router.get("/jokes/chuck-norris",
            summary="Get Chuck Norris joke")
async def get_chuck_norris_joke():
    """
    Get random Chuck Norris joke
    
    **Real API URL:** `https://api.chucknorris.io/jokes/random`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://api.chucknorris.io/jokes/random')
    joke = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://api.chucknorris.io/jokes/random"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Chuck Norris IO"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chuck Norris API error: {str(e)}")


# ==================== QUOTES ====================

@router.get("/quotes/random",
            summary="Get random quote")
async def get_random_quote():
    """
    Get random inspirational quote
    
    **Real API URL:** `https://api.quotable.io/random`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://api.quotable.io/random')
    quote = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://api.quotable.io/random"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Quotable"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Quotable API error: {str(e)}")


# ==================== FACTS ====================

@router.get("/facts/random",
            summary="Get random fact")
async def get_random_fact():
    """
    Get random interesting fact
    
    **Real API URL:** `https://uselessfacts.jsph.pl/random.json?language=en`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    fact = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://uselessfacts.jsph.pl/random.json?language=en"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Useless Facts"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Useless Facts API error: {str(e)}")
