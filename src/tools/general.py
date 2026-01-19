"""General MCP tools."""

from fastmcp import FastMCP


def register_general_tools(mcp: FastMCP) -> None:
    """Register general-purpose tools."""

    @mcp.tool
    def greet(name: str) -> str:
        """Return a friendly greeting."""
        return f"Hello, {name}!"
