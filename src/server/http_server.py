"""HTTP/SSE server wrapper for MCP server."""

from starlette.responses import HTMLResponse, JSONResponse
import uvicorn

from src.server.mcp_server import mcp


def root(_request) -> HTMLResponse:
    """Simple landing page for the MCP server."""
    return HTMLResponse(
        """
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Home Device Bridge</title>
            <style>
              body { font-family: Arial, sans-serif; margin: 40px; color: #111; }
              h1 { margin-bottom: 8px; }
              p { margin: 6px 0; }
              code { background: #f2f2f2; padding: 2px 6px; border-radius: 4px; }
            </style>
          </head>
          <body>
            <h1>Home Device Bridge</h1>
            <p>MCP server is running.</p>
            <p>SSE endpoint: <code>/sse</code></p>
          </body>
        </html>
        """
    )


def health(_request) -> JSONResponse:
    """Basic health check for browsers and uptime monitors."""
    return JSONResponse({"status": "ok"})


def create_app():
    """Create the Starlette app with MCP routes and a simple landing page."""
    app = mcp.http_app(transport="sse")
    app.add_route("/", root, methods=["GET"])
    app.add_route("/health", health, methods=["GET"])
    return app


if __name__ == "__main__":
    uvicorn.run(create_app(), host="0.0.0.0", port=8000)
