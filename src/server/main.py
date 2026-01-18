"""Main MCP server application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.server.config import settings
from src.server.routes import health, devices, notifications


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Home Device Bridge",
        description="MCP server for communication between home devices",
        version="0.1.0",
    )

    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(health.router, tags=["health"])
    app.include_router(devices.router, prefix="/devices", tags=["devices"])
    app.include_router(notifications.router, prefix="/notifications", tags=["notifications"])

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.server.main:app",
        host=settings.MCP_HOST,
        port=settings.MCP_PORT,
        reload=settings.MCP_DEBUG,
    )
