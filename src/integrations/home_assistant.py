"""Home Assistant integration."""

import httpx
from src.server.config import settings


class HomeAssistantClient:
    """Client for Home Assistant API."""

    def __init__(self) -> None:
        """Initialize Home Assistant client."""
        self.base_url = settings.HA_URL
        self.token = settings.HA_TOKEN
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    async def get_devices(self) -> list:
        """
        Get list of devices from Home Assistant.

        Returns:
            List of device entities
        """
        # TODO: Implement device discovery
        pass

    async def send_notification(
        self,
        device: str,
        title: str,
        message: str,
        data: dict | None = None
    ) -> dict:
        """
        Send notification via Home Assistant.

        Args:
            device: Device ID (e.g., 'iphone_2')
            title: Notification title
            message: Notification message
            data: Additional notification data

        Returns:
            Response from Home Assistant
        """
        # TODO: Implement notification sending
        pass

    async def get_state(self, entity_id: str) -> dict:
        """
        Get state of an entity.

        Args:
            entity_id: Entity ID

        Returns:
            Entity state information
        """
        # TODO: Implement state retrieval
        pass
