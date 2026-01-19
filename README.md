# Home Device Bridge

Minimal FastMCP server packaged for Docker deployment.

## What stays

- FastMCP server with a basic `greet` tool
- HTTP transport (stateless JSON responses)
- Dockerfile and docker-compose

## Docker

```bash
docker build -t home-device-bridge .
docker run -p 8000:8000 home-device-bridge
```

Set `PORT` to override the internal listening port (default: `8000`).

## Docker Compose

```bash
docker-compose up -d --build
```

## Local deploy

```bash
./scripts/deploy.sh
```

Use `./scripts/deploy.sh --rebuild` for a clean rebuild on the server.

## Endpoints

- HTTP MCP: `http://localhost:8000/mcp`

## Home Assistant

Set environment variables for notifications:

```bash
HA_URL=http://homeassistant.local:8123
HA_TOKEN=your_long_lived_access_token
```
