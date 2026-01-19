"""FastMCP entrypoint."""

from dotenv import load_dotenv
from fastmcp import FastMCP

from src.prompts.notifications import register_notification_prompts
from src.resources.notifications import register_notification_resources
from src.tools.general import register_general_tools
from src.tools.notifications import register_notification_tools

load_dotenv()

mcp = FastMCP("My MCP Server")
register_general_tools(mcp)
register_notification_tools(mcp)
register_notification_resources(mcp)
register_notification_prompts(mcp)

if __name__ == "__main__":
    mcp.run(transport="http")
