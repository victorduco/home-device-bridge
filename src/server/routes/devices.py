"""Device management endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_devices() -> dict[str, list]:
    """
    Get list of all connected devices.

    Returns:
        Dictionary with devices list
    """
    # TODO: Implement device discovery from Home Assistant
    return {
        "devices": []
    }


@router.get("/{device_id}")
async def get_device(device_id: str) -> dict[str, str]:
    """
    Get device information by ID.

    Args:
        device_id: Device identifier

    Returns:
        Device information
    """
    # TODO: Implement device info retrieval
    return {
        "device_id": device_id,
        "status": "unknown"
    }
