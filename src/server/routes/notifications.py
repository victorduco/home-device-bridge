"""Notification endpoints."""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class NotificationRequest(BaseModel):
    """Notification request model."""

    device: str
    title: str
    message: str
    data: dict = {}


@router.post("/send")
async def send_notification(notification: NotificationRequest) -> dict[str, str]:
    """
    Send notification to a device.

    Args:
        notification: Notification details

    Returns:
        Send status
    """
    # TODO: Implement notification sending via Home Assistant
    return {
        "status": "pending",
        "device": notification.device,
        "message": "Notification queued"
    }


@router.get("/history")
async def get_notification_history() -> dict[str, list]:
    """
    Get notification history.

    Returns:
        List of sent notifications
    """
    # TODO: Implement notification history tracking
    return {
        "notifications": []
    }
