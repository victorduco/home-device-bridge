"""Resources describing Home Assistant notifications."""

from fastmcp import FastMCP

from ..config import NOTIFICATION_GUIDE


def register_notification_resources(mcp: FastMCP) -> None:
    """Register notification-related resources."""

    @mcp.resource("notification/guide")
    def notification_guide() -> str:
        """Return a concise guide for crafting notifications."""
        return NOTIFICATION_GUIDE
