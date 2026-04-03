"""
E-commerce & Products Routes
Documentation for e-commerce and product public APIs

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/ecommerce", tags=["E-commerce"])
http_client = get_http_client()


# ==================== FAKE STORE API ====================

@router.get("/products",
            summary="Get all products from Fake Store API")
async def get_all_products(
    limit: int = Query(None, ge=1, le=20, description="Limit number of results")
):
    """
    Get all products from Fake Store API
    
    **Real API URL:** `https://fakestoreapi.com/products`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://fakestoreapi.com/products')
    products = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://fakestoreapi.com/products"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        data = response.json()
        if limit:
            data = data[:limit]
        
        return JSONResponse(
            content=data,
            headers={"x-api-url": real_url, "x-api-provider": "Fake Store API"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fake Store API error: {str(e)}")


@router.get("/products/{product_id}",
            summary="Get product by ID from Fake Store API")
async def get_product_by_id(
    product_id: int = Path(..., ge=1, description="Product ID")
):
    """
    Get a specific product by ID
    
    **Real API URL:** `https://fakestoreapi.com/products/{id}`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://fakestoreapi.com/products/1')
    product = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = f"https://fakestoreapi.com/products/{product_id}"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Fake Store API"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fake Store API error: {str(e)}")


@router.get("/categories",
            summary="Get all product categories")
async def get_product_categories():
    """
    Get all product categories from Fake Store API
    
    **Real API URL:** `https://fakestoreapi.com/products/categories`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://fakestoreapi.com/products/categories')
    categories = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://fakestoreapi.com/products/categories"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Fake Store API"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fake Store API error: {str(e)}")


# ==================== DUMMYJSON ====================

@router.get("/dummy/products",
            summary="Get products from DummyJSON")
async def get_dummy_products(
    limit: int = Query(10, ge=1, le=100, description="Number of results"),
    skip: int = Query(0, ge=0, description="Number of results to skip")
):
    """
    Get products from DummyJSON API
    
    **Real API URL:** `https://dummyjson.com/products`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://dummyjson.com/products',
        params={'limit': 10, 'skip': 0}
    )
    products = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://dummyjson.com/products"
        response = await http_client.get(
            real_url,
            params={"limit": limit, "skip": skip}
        )
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "DummyJSON"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DummyJSON API error: {str(e)}")


# ==================== JSONPLACEHOLDER ====================

@router.get("/posts",
            summary="Get posts from JSONPlaceholder")
async def get_posts(
    limit: int = Query(10, ge=1, le=100, description="Number of results")
):
    """
    Get posts from JSONPlaceholder
    
    **Real API URL:** `https://jsonplaceholder.typicode.com/posts`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://jsonplaceholder.typicode.com/posts',
        params={'_limit': 10}
    )
    posts = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://jsonplaceholder.typicode.com/posts"
        response = await http_client.get(
            real_url,
            params={"_limit": limit}
        )
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "JSONPlaceholder"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"JSONPlaceholder API error: {str(e)}")


@router.get("/users",
            summary="Get users from JSONPlaceholder")
async def get_users(
    limit: int = Query(10, ge=1, le=100, description="Number of results")
):
    """
    Get users from JSONPlaceholder
    
    **Real API URL:** `https://jsonplaceholder.typicode.com/users`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users',
        params={'_limit': 10}
    )
    users = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://jsonplaceholder.typicode.com/users"
        response = await http_client.get(
            real_url,
            params={"_limit": limit}
        )
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "JSONPlaceholder"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"JSONPlaceholder API error: {str(e)}")
