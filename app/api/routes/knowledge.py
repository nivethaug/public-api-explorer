"""
Knowledge & Education Routes
Documentation for educational and reference public APIs

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/knowledge", tags=["Knowledge & Education"])
http_client = get_http_client()


# ==================== DICTIONARY ====================

@router.get("/dictionary/{word}",
            summary="Get word definition from Free Dictionary API")
async def get_word_definition(
    word: str = Path(..., description="Word to look up")
):
    """
    Get definition, pronunciation, and examples for a word
    
    **Real API URL:** `https://api.dictionaryapi.dev/api/v2/entries/en/{word}`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/hello')
    definition = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Free Dictionary API"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Dictionary API error: {str(e)}")


# ==================== OPEN LIBRARY ====================

@router.get("/books/search",
            summary="Search books on Open Library")
async def search_books(
    query: str = Query(..., description="Search query (title, author, or ISBN)"),
    limit: int = Query(10, ge=1, le=100, description="Number of results")
):
    """
    Search for books in Open Library
    
    **Real API URL:** `https://openlibrary.org/search.json`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://openlibrary.org/search.json',
        params={'q': 'python programming', 'limit': 10}
    )
    books = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://openlibrary.org/search.json"
        response = await http_client.get(
            real_url,
            params={"q": query, "limit": limit}
        )
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Open Library"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Open Library API error: {str(e)}")


@router.get("/books/{work_id}",
            summary="Get book details by Work ID")
async def get_book_details(
    work_id: str = Path(..., description="Open Library Work ID (e.g., 'OL45804W')")
):
    """
    Get detailed information about a book by its Work ID
    
    **Real API URL:** `https://openlibrary.org/works/{work_id}.json`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://openlibrary.org/works/OL45804W.json')
    book = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = f"https://openlibrary.org/works/{work_id}.json"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Open Library"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Open Library API error: {str(e)}")


# ==================== WIKIPEDIA ====================

@router.get("/wikipedia/search",
            summary="Search Wikipedia articles")
async def search_wikipedia(
    query: str = Query(..., description="Search query"),
    limit: int = Query(10, ge=1, le=50, description="Number of results")
):
    """
    Search Wikipedia articles
    
    **Real API URL:** `https://en.wikipedia.org/w/api.php`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://en.wikipedia.org/w/api.php',
        params={
            'action': 'opensearch',
            'search': 'python programming',
            'limit': 10,
            'format': 'json'
        }
    )
    results = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://en.wikipedia.org/w/api.php"
        response = await http_client.get(
            real_url,
            params={
                "action": "opensearch",
                "search": query,
                "limit": limit,
                "format": "json"
            }
        )
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Wikipedia"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Wikipedia API error: {str(e)}")


@router.get("/wikipedia/article/{title}",
            summary="Get Wikipedia article summary")
async def get_wikipedia_article(
    title: str = Path(..., description="Article title")
):
    """
    Get a summary of a Wikipedia article
    
    **Real API URL:** `https://en.wikipedia.org/api/rest_v1/page/summary/{title}`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://en.wikipedia.org/api/rest_v1/page/summary/Python_(programming_language)'
    )
    article = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Wikipedia"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Wikipedia API error: {str(e)}")
