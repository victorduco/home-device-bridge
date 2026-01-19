"""Application factory for the FastMCP server."""

from fastmcp import FastMCP

from .prompts.notifications import register_notification_prompts
from .resources.notifications import register_notification_resources
from .tools.general import register_general_tools
from .tools.notifications import register_notification_tools


def create_app() -> FastMCP:
    """Create and configure the FastMCP app."""
    mcp = FastMCP("My MCP Server")
    register_general_tools(mcp)
    register_notification_tools(mcp)
    register_notification_resources(mcp)
    register_notification_prompts(mcp)
    return mcp
