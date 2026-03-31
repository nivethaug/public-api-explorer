"""
Category Template
Copy this file to create a new API category
"""

from fastapi import APIRouter, HTTPException, Query, Path
from app.core.http_client import get_http_client

# Change the prefix and tags to match your category
router = APIRouter(prefix="/category-name", tags=["Category Name"])
http_client = get_http_client()


# Example endpoint template
@router.get("/endpoint",
            summary="Brief summary of endpoint")
async def endpoint_name(
    param1: str = Query(..., description="Parameter description"),
    param2: int = Query(10, ge=1, le=100, description="Another parameter")
):
    """
    Detailed description of what this endpoint does.
    
    - **param1**: Description of param1
    - **param2**: Description of param2
    """
    try:
        response = await http_client.get(
            "https://api.example.com/endpoint",
            params={"param1": param1, "param2": param2}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"API error: {str(e)}")


# Add more endpoints as needed
