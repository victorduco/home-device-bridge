"""Health check endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check() -> dict[str, str]:
    """
    Health check endpoint.

    Returns:
        Dictionary with status information
    """
    return {
        "status": "healthy",
        "service": "home-device-bridge",
        "version": "0.1.0"
    }


@router.get("/")
async def root() -> dict[str, str]:
    """
    Root endpoint.

    Returns:
        Welcome message
    """
    return {
        "message": "Home Device Bridge MCP Server",
        "version": "0.1.0"
    }
