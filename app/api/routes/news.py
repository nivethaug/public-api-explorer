"""
News Routes
Documentation for news public APIs

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/news", tags=["News"])
http_client = get_http_client()


@router.get("/hackernews/top",
            summary="Get top stories from HackerNews")
async def get_hackernews_top(
    limit: int = Query(30, ge=1, le=500, description="Number of stories to fetch")
):
    """
    Get top story IDs from HackerNews
    
    **Real API URL:** `https://hacker-news.firebaseio.com/v0/topstories.json`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Get top story IDs
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    story_ids = response.json()[:30]
    
    # Fetch each story
    stories = []
    for story_id in story_ids:
        story = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json').json()
        stories.append(story)
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        # Get top story IDs
        response = await http_client.get(real_url)
        response.raise_for_status()
        story_ids = response.json()[:limit]
        
        # Fetch story details
        stories = []
        for story_id in story_ids:
            story_response = await http_client.get(
                f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            )
            if story_response.status_code == 200:
                stories.append(story_response.json())
        
        return JSONResponse(
            content={"count": len(stories), "stories": stories},
            headers={"x-api-url": real_url, "x-api-provider": "HackerNews"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"HackerNews API error: {str(e)}")


@router.get("/hackernews/new",
            summary="Get new stories from HackerNews")
async def get_hackernews_new(
    limit: int = Query(30, ge=1, le=500, description="Number of stories to fetch")
):
    """Get new story IDs from HackerNews"""
    try:
        response = await http_client.get(
            "https://hacker-news.firebaseio.com/v0/newstories.json"
        )
        response.raise_for_status()
        story_ids = response.json()[:limit]
        
        stories = []
        for story_id in story_ids:
            story_response = await http_client.get(
                f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            )
            if story_response.status_code == 200:
                stories.append(story_response.json())
        
        return {"count": len(stories), "stories": stories}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"HackerNews API error: {str(e)}")


@router.get("/hackernews/item/{item_id}",
            summary="Get specific HackerNews item")
async def get_hackernews_item(
    item_id: int = Path(..., description="Item ID")
):
    """Get details of a specific HackerNews item (story, comment, etc.)"""
    try:
        response = await http_client.get(
            f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"HackerNews API error: {str(e)}")
