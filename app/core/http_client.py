"""
HTTP Client Manager
Shared async HTTP client for all API routes
"""

import httpx
from typing import Optional
from app.core.config import settings


class HTTPClientManager:
    """Manages the shared HTTP client instance"""
    
    _instance: Optional[httpx.AsyncClient] = None
    
    @classmethod
    def get_client(cls) -> httpx.AsyncClient:
        """Get or create the HTTP client instance"""
        if cls._instance is None:
            cls._instance = httpx.AsyncClient(
                timeout=settings.HTTP_TIMEOUT,
                follow_redirects=True
            )
        return cls._instance
    
    @classmethod
    async def close(cls):
        """Close the HTTP client"""
        if cls._instance is not None:
            await cls._instance.aclose()
            cls._instance = None


# Convenience function to get client
def get_http_client() -> httpx.AsyncClient:
    """Get the shared HTTP client"""
    return HTTPClientManager.get_client()
