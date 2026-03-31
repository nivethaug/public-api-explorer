"""
AI & NLP Routes
Documentation for AI and natural language processing public APIs

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/ai", tags=["AI & NLP"])
http_client = get_http_client()


# ==================== TEXT ANALYSIS ====================

@router.get("/text/sentiment",
            summary="Analyze text sentiment")
async def analyze_sentiment(
    text: str = Query(..., description="Text to analyze")
):
    """
    Analyze sentiment of text using basic NLP
    
    **Real API URL:** `https://api.textgain.com/v1/sentiment`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://api.textgain.com/v1/sentiment',
        params={'text': 'I love this product!'}
    )
    sentiment = response.json()
    ```
    
    **Note:** Some NLP APIs may require authentication
    """
    try:
        # Alternative: Using a simple sentiment API
        real_url = "https://api.textgain.com/v1/sentiment"
        return JSONResponse(
            content={
                "message": "Text sentiment analysis",
                "real_url": real_url,
                "text": text,
                "alternative": "Use libraries like TextBlob or VADER in Python"
            },
            headers={"x-api-url": real_url, "x-api-provider": "TextGain"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sentiment API error: {str(e)}")


# ==================== TRANSLATION ====================

@router.get("/translate",
            summary="Translate text")
async def translate_text(
    text: str = Query(..., description="Text to translate"),
    target_lang: str = Query("es", description="Target language code")
):
    """
    Translate text using free translation APIs
    
    **Real API URL:** `https://api.mymemory.translated.net/get`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://api.mymemory.translated.net/get',
        params={
            'q': 'Hello World',
            'langpair': 'en|es'
        }
    )
    translation = response.json()
    ```
    
    **No authentication required** (with rate limits)
    """
    try:
        real_url = "https://api.mymemory.translated.net/get"
        response = await http_client.get(
            real_url,
            params={
                "q": text,
                "langpair": f"en|{target_lang}"
            }
        )
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "MyMemory"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation API error: {str(e)}")


# ==================== QR CODES ====================

@router.get("/qrcode",
            summary="Generate QR code")
async def generate_qrcode(
    text: str = Query(..., description="Text to encode in QR code")
):
    """
    Generate QR code image
    
    **Real API URL:** `https://api.qrserver.com/v1/create-qr-code/`
    
    **Direct Usage Example:**
    ```python
    import requests
    from PIL import Image
    from io import BytesIO
    
    # Call the real API directly
    response = requests.get(
        'https://api.qrserver.com/v1/create-qr-code/',
        params={'size': '200x200', 'data': 'https://example.com'}
    )
    img = Image.open(BytesIO(response.content))
    ```
    
    **No authentication required**
    """
    try:
        real_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={text}"
        return JSONResponse(
            content={
                "message": "QR code generation",
                "real_url": real_url,
                "how_to_use": f"Open {real_url} in browser or download image"
            },
            headers={"x-api-url": real_url, "x-api-provider": "QR Server"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"QR Code API error: {str(e)}")


# ==================== RANDOM DATA ====================

@router.get("/random/user",
            summary="Generate random user data")
async def generate_random_user():
    """
    Generate random user data for testing
    
    **Real API URL:** `https://randomuser.me/api/`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://randomuser.me/api/')
    user = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://randomuser.me/api/"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Random User"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Random User API error: {str(e)}")
