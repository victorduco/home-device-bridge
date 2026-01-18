"""HTTP/SSE server wrapper for MCP server."""

from fastmcp import FastMCP
from src.server.mcp_server import mcp

if __name__ == "__main__":
    # Run MCP server over HTTP with SSE transport
    mcp.run(transport="sse", host="0.0.0.0", port=8000)
