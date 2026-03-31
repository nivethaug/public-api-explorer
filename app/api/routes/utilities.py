"""
Utilities Routes
Documentation for utility public APIs and tools

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client
import uuid
import hashlib
from datetime import datetime
import base64

router = APIRouter(prefix="/utilities", tags=["Utilities"])
http_client = get_http_client()


# ==================== QR CODES ====================

@router.get("/qr/generate",
            summary="Generate QR code")
async def generate_qr_code(
    text: str = Query(..., description="Text to encode in QR code"),
    size: int = Query(150, ge=50, le=500, description="QR code size in pixels")
):
    """
    Generate a QR code image
    
    **Real API URL:** `https://api.qrserver.com/v1/create-qr-code/`
    
    **Direct Usage Example:**
    ```python
    import requests
    from PIL import Image
    from io import BytesIO
    
    # Call the real API directly
    params = {
        'size': f'{size}x{size}',
        'data': text
    }
    response = requests.get(
        'https://api.qrserver.com/v1/create-qr-code/',
        params=params
    )
    img = Image.open(BytesIO(response.content))
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://api.qrserver.com/v1/create-qr-code/"
        params = {
            'size': f'{size}x{size}',
            'data': text
        }
        response = await http_client.get(real_url, params=params)
        response.raise_for_status()
        
        # Return image as base64
        img_base64 = base64.b64encode(response.content).decode('utf-8')
        
        return JSONResponse(
            content={
                "qr_code_base64": img_base64,
                "text_encoded": text,
                "size": f"{size}x{size}",
                "format": "PNG",
                "real_url": real_url
            },
            headers={"x-api-url": real_url, "x-api-provider": "QRServer"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"QR API error: {str(e)}")


# ==================== COLORS ====================

@router.get("/color/info",
            summary="Get color information")
async def get_color_info(
    hex_color: str = Query(..., description="Hex color code (with or without #)", regex="^#?[0-9A-Fa-f]{6}$")
):
    """
    Get detailed information about a color
    
    **Real API URL:** `https://www.thecolorapi.com/id`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://www.thecolorapi.com/id',
        params={'hex': 'FF5733'}
    )
    color_data = response.json()
    ```
    
    **No authentication required**
    """
    try:
        # Remove # if present
        hex_clean = hex_color.lstrip('#')
        
        real_url = "https://www.thecolorapi.com/id"
        params = {'hex': hex_clean}
        
        response = await http_client.get(real_url, params=params)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": f"{real_url}?hex={hex_clean}", "x-api-provider": "TheColorAPI"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Color API error: {str(e)}")


# ==================== UUID ====================

@router.get("/uuid/generate",
            summary="Generate UUID")
async def generate_uuid(
    version: int = Query(4, ge=1, le=5, description="UUID version (1, 3, 4, or 5)")
):
    """
    Generate a unique identifier (UUID)
    
    **Local Generation (Python):**
    ```python
    import uuid
    
    # UUID v4 (random) - most common
    new_uuid = uuid.uuid4()
    print(str(new_uuid))  # e.g., '550e8400-e29b-41d4-a716-446655440000'
    
    # UUID v1 (time-based)
    time_uuid = uuid.uuid1()
    
    # UUID v3 (name-based, MD5)
    name_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, 'example.com')
    
    # UUID v5 (name-based, SHA-1)
    name_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com')
    ```
    
    **No external API needed - generated locally**
    """
    try:
        if version == 4:
            new_uuid = uuid.uuid4()
        elif version == 1:
            new_uuid = uuid.uuid1()
        elif version == 3:
            new_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, 'example.com')
        elif version == 5:
            new_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com')
        else:
            raise HTTPException(status_code=400, detail="UUID version must be 1, 3, 4, or 5")
        
        return JSONResponse(
            content={
                "uuid": str(new_uuid),
                "version": version,
                "urn": new_uuid.urn,
                "hex": new_uuid.hex,
                "int": new_uuid.int
            },
            headers={"x-api-provider": "Python uuid module"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"UUID generation error: {str(e)}")


# ==================== HASHING ====================

@router.get("/hash/text",
            summary="Hash text")
async def hash_text(
    text: str = Query(..., description="Text to hash"),
    algorithm: str = Query("sha256", description="Hash algorithm (md5, sha1, sha256, sha512)")
):
    """
    Hash text using various algorithms
    
    **Local Generation (Python):**
    ```python
    import hashlib
    
    # SHA-256 (recommended)
    hash_obj = hashlib.sha256('hello'.encode())
    print(hash_obj.hexdigest())
    
    # SHA-512
    hash_obj = hashlib.sha512('hello'.encode())
    print(hash_obj.hexdigest())
    
    # MD5 (not recommended for security)
    hash_obj = hashlib.md5('hello'.encode())
    print(hash_obj.hexdigest())
    
    # SHA-1 (not recommended for security)
    hash_obj = hashlib.sha1('hello'.encode())
    print(hash_obj.hexdigest())
    ```
    
    **No external API needed - generated locally**
    """
    try:
        algorithm = algorithm.lower()
        valid_algorithms = ['md5', 'sha1', 'sha256', 'sha512']
        
        if algorithm not in valid_algorithms:
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid algorithm. Must be one of: {', '.join(valid_algorithms)}"
            )
        
        hash_obj = hashlib.new(algorithm, text.encode())
        hash_value = hash_obj.hexdigest()
        
        return JSONResponse(
            content={
                "original_text": text,
                "algorithm": algorithm,
                "hash": hash_value,
                "length": len(hash_value)
            },
            headers={"x-api-provider": "Python hashlib module"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Hashing error: {str(e)}")


# ==================== TIMESTAMP ====================

@router.get("/timestamp/current",
            summary="Get current timestamp")
async def get_current_timestamp(
    timezone: str = Query("UTC", description="Timezone (UTC, local)")
):
    """
    Get current timestamp in various formats
    
    **Local Generation (Python):**
    ```python
    from datetime import datetime
    import time
    
    # Current datetime
    now = datetime.now()
    
    # Unix timestamp (seconds since epoch)
    timestamp = int(time.time())
    
    # ISO format
    iso_format = now.isoformat()
    
    # Formatted string
    formatted = now.strftime('%Y-%m-%d %H:%M:%S')
    ```
    
    **No external API needed - generated locally**
    """
    try:
        now = datetime.utcnow() if timezone.upper() == "UTC" else datetime.now()
        
        return JSONResponse(
            content={
                "unix_timestamp": int(now.timestamp()),
                "iso_format": now.isoformat(),
                "utc": now.strftime('%Y-%m-%dT%H:%M:%SZ'),
                "formatted": now.strftime('%Y-%m-%d %H:%M:%S'),
                "date": now.strftime('%Y-%m-%d'),
                "time": now.strftime('%H:%M:%S'),
                "timezone": timezone,
                "day_of_week": now.strftime('%A'),
                "month_name": now.strftime('%B'),
                "year": now.year
            },
            headers={"x-api-provider": "Python datetime module"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Timestamp error: {str(e)}")
