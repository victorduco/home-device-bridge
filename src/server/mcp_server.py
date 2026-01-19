"""FastMCP server entrypoint."""

from .app import create_app


if __name__ == "__main__":
    mcp = create_app()
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000,
        json_response=True,
        stateless_http=True,
    )
