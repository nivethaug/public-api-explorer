"""
Images Routes
Documentation for image public APIs

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/images", tags=["Images"])
http_client = get_http_client()


# ==================== UNSPLASH ====================

@router.get("/unsplash/random",
            summary="Get random image from Unsplash")
async def get_unsplash_random():
    """
    Get random high-quality image from Unsplash
    
    **Real API URL:** `https://api.unsplash.com/photos/random`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    # Get free access key from https://unsplash.com/developers
    headers = {'Authorization': 'Client-ID YOUR_ACCESS_KEY'}
    response = requests.get('https://api.unsplash.com/photos/random', headers=headers)
    image = response.json()
    ```
    
    **Note:** Requires free Unsplash API key
    """
    try:
        real_url = "https://api.unsplash.com/photos/random"
        return JSONResponse(
            content={
                "message": "Unsplash API requires authentication",
                "real_url": real_url,
                "how_to_use": {
                    "step1": "Get free access key from https://unsplash.com/developers",
                    "step2": f"Call: {real_url} with header 'Authorization: Client-ID YOUR_KEY'",
                    "example": f"requests.get('{real_url}', headers={{'Authorization': 'Client-ID YOUR_KEY'}})"
                }
            },
            headers={"x-api-url": real_url, "x-api-provider": "Unsplash"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unsplash API error: {str(e)}")


# ==================== PICSUM ====================

@router.get("/picsum",
            summary="Get random image from Picsum")
async def get_picsum_image():
    """
    Get random image from Picsum (Lorem Picsum)
    
    **Real API URL:** `https://picsum.photos/200/300`
    
    **Direct Usage Example:**
    ```python
    import requests
    from PIL import Image
    from io import BytesIO
    
    # Call the real API directly - returns image directly
    response = requests.get('https://picsum.photos/200/300')
    img = Image.open(BytesIO(response.content))
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://picsum.photos/200/300"
        return JSONResponse(
            content={
                "message": "Picsum returns images directly",
                "real_url": real_url,
                "how_to_use": {
                    "description": "Returns actual image, not JSON",
                    "example": f"requests.get('{real_url}') - returns image binary",
                    "random": "https://picsum.photos/{width}/{height}"
                }
            },
            headers={"x-api-url": real_url, "x-api-provider": "Picsum"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Picsum API error: {str(e)}")


# ==================== DOG CEO ====================

@router.get("/dogceo/random",
            summary="Get random dog image")
async def get_random_dog():
    """
    Get random dog image from Dog CEO
    
    **Real API URL:** `https://dog.ceo/api/breeds/image/random`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    dog_image = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://dog.ceo/api/breeds/image/random"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Dog CEO"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Dog CEO API error: {str(e)}")


# ==================== CAT AS A SERVICE ====================

@router.get("/cataas/random",
            summary="Get random cat image")
async def get_random_cat():
    """
    Get random cat image from Cat as a Service
    
    **Real API URL:** `https://cataas.com/cat`
    
    **Direct Usage Example:**
    ```python
    import requests
    from PIL import Image
    from io import BytesIO
    
    # Call the real API directly - returns image
    response = requests.get('https://cataas.com/cat')
    img = Image.open(BytesIO(response.content))
    
    # Or get JSON with URL
    response = requests.get('https://cataas.com/cat?json=true')
    cat_data = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://cataas.com/cat?json=true"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Cat as a Service"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cat API error: {str(e)}")
