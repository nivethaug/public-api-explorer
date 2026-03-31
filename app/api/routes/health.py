"""
Health Check Routes
System health and status endpoints
"""

from fastapi import APIRouter
from datetime import datetime
from app.core.config import settings

router = APIRouter(tags=["Health"])


@router.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "timestamp": datetime.utcnow().isoformat(),
        "docs": settings.DOCS_URL
    }
