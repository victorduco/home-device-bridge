"""Home Assistant notification tools."""

from typing import Any

import httpx
from fastmcp import FastMCP

from ..config import HA_TOKEN, HA_URL


def register_notification_tools(mcp: FastMCP) -> None:
    """Register Home Assistant notification tools."""

    @mcp.tool
    async def send_notification(
        device: str,
        title: str,
        message: str,
        subtitle: str = "",
        sound: str = "default",
        data: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Send a Home Assistant push notification using notify.mobile_app_<device>."""
        if not HA_TOKEN:
            return {"status": "error", "error": "HA_TOKEN is not set"}

        headers = {
            "Authorization": f"Bearer {HA_TOKEN}",
            "Content-Type": "application/json",
        }

        payload: dict[str, Any] = {
            "message": message,
            "title": title,
            "data": dict(data or {}),
        }

        if sound:
            payload["data"].setdefault("push", {})
            payload["data"]["push"]["sound"] = sound
        if subtitle:
            payload["data"]["subtitle"] = subtitle

        service_name = f"mobile_app_{device}"
        url = f"{HA_URL}/api/services/notify/{service_name}"

        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return {
                "status": "success",
                "device": device,
                "message": "Notification sent",
            }
        return {
            "status": "error",
            "device": device,
            "error": f"HTTP {response.status_code}: {response.text}",
        }
