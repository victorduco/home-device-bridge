"""FastMCP server for home device communication."""

import os
from fastmcp import FastMCP
from dotenv import load_dotenv
import httpx

# Load environment variables
load_dotenv()

# Initialize MCP server
mcp = FastMCP("Home Device Bridge")

# Configuration
HA_URL = os.getenv("HA_URL", "http://homeassistant.local:8123")
HA_TOKEN = os.getenv("HA_TOKEN", "")


@mcp.tool()
async def send_notification(
    device: str,
    title: str,
    message: str,
    subtitle: str = "",
    sound: str = "default"
) -> dict:
    """
    Send notification to a mobile device via Home Assistant.

    Args:
        device: Device ID (e.g., 'iphone_2', 'sm_t860')
        title: Notification title
        message: Notification message
        subtitle: Optional subtitle (iOS only)
        sound: Notification sound (default: 'default')

    Returns:
        Status of the notification
    """
    headers = {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "message": message,
        "title": title,
        "data": {
            "push": {"sound": sound}
        }
    }

    if subtitle:
        payload["data"]["subtitle"] = subtitle

    service_name = f"mobile_app_{device}"
    url = f"{HA_URL}/api/services/notify/{service_name}"

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return {
                "status": "success",
                "device": device,
                "message": "Notification sent successfully"
            }
        else:
            return {
                "status": "error",
                "device": device,
                "error": f"HTTP {response.status_code}: {response.text}"
            }


@mcp.tool()
async def get_devices() -> dict:
    """
    Get list of available mobile devices from Home Assistant.

    Returns:
        List of available devices
    """
    headers = {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type": "application/json"
    }

    url = f"{HA_URL}/api/services"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

        if response.status_code == 200:
            services = response.json()
            notify_services = []

            for service in services:
                if service.get("domain") == "notify":
                    service_keys = service.get("services", {}).keys()
                    mobile_services = [
                        key for key in service_keys
                        if key.startswith("mobile_app_")
                    ]
                    notify_services.extend(mobile_services)

            return {
                "status": "success",
                "devices": [
                    {
                        "id": svc.replace("mobile_app_", ""),
                        "service_name": svc
                    }
                    for svc in notify_services
                ]
            }
        else:
            return {
                "status": "error",
                "error": f"HTTP {response.status_code}: {response.text}"
            }


@mcp.tool()
async def get_entity_state(entity_id: str) -> dict:
    """
    Get state of a Home Assistant entity.

    Args:
        entity_id: Entity ID (e.g., 'light.living_room', 'sensor.temperature')

    Returns:
        Entity state and attributes
    """
    headers = {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type": "application/json"
    }

    url = f"{HA_URL}/api/states/{entity_id}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return {
                "status": "success",
                "entity_id": entity_id,
                "state": data.get("state"),
                "attributes": data.get("attributes", {}),
                "last_changed": data.get("last_changed")
            }
        else:
            return {
                "status": "error",
                "error": f"HTTP {response.status_code}: {response.text}"
            }


@mcp.tool()
async def call_service(domain: str, service: str, entity_id: str = "", data: dict = None) -> dict:
    """
    Call a Home Assistant service.

    Args:
        domain: Service domain (e.g., 'light', 'switch', 'automation')
        service: Service name (e.g., 'turn_on', 'turn_off', 'toggle')
        entity_id: Optional entity ID to target
        data: Optional service data

    Returns:
        Service call result
    """
    headers = {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type": "application/json"
    }

    url = f"{HA_URL}/api/services/{domain}/{service}"

    payload = data or {}
    if entity_id:
        payload["entity_id"] = entity_id

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return {
                "status": "success",
                "domain": domain,
                "service": service,
                "message": "Service called successfully"
            }
        else:
            return {
                "status": "error",
                "error": f"HTTP {response.status_code}: {response.text}"
            }


@mcp.resource("config://homeassistant")
async def get_ha_config() -> str:
    """Get Home Assistant configuration info."""
    headers = {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type": "application/json"
    }

    url = f"{HA_URL}/api/config"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

        if response.status_code == 200:
            return response.text
        else:
            return f"Error: HTTP {response.status_code}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
