# Home Device Bridge

FastMCP server for communication and control of home devices via Model Context Protocol.

## Overview

Home Device Bridge is a FastMCP-based MCP server that provides AI-accessible tools for controlling and monitoring home devices through Home Assistant. Built with the official FastMCP Python SDK, it exposes tools, resources, and prompts for seamless device interaction.

## Features

- 🏠 **Home Assistant Integration** - Full API integration with Home Assistant
- 📱 **Mobile Notifications** - Send notifications to iOS/Android devices
- 🔧 **MCP Tools** - AI-accessible tools for device control
- 📊 **Entity State** - Query and monitor device states
- 🎯 **Service Calls** - Execute Home Assistant services
- 🌐 **HTTP/SSE Transport** - Accessible via HTTP with Server-Sent Events

## MCP Tools

### `send_notification`
Send notifications to mobile devices via Home Assistant.

```python
{
  "device": "iphone_2",
  "title": "Alert",
  "message": "Motion detected!",
  "subtitle": "Living Room",
  "sound": "default"
}
```

### `get_devices`
List all available mobile devices from Home Assistant.

### `get_entity_state`
Get current state and attributes of any Home Assistant entity.

```python
{
  "entity_id": "light.living_room"
}
```

### `call_service`
Call any Home Assistant service.

```python
{
  "domain": "light",
  "service": "turn_on",
  "entity_id": "light.living_room"
}
```

## Installation

```bash
# Clone repository
git clone https://github.com/victorduco/home-device-bridge.git
cd home-device-bridge

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .
```

## Configuration

Create `.env` file:

```env
# Home Assistant
HA_URL=http://homeassistant.local:8123
HA_TOKEN=your_long_lived_access_token
```

## Usage

### Run with stdio transport (for local CLI)
```bash
python -m src.server.mcp_server
```

### Run with HTTP/SSE transport (for remote access)
```bash
python -m src.server.http_server
```

Server will be available at `http://localhost:8000`

## Docker Deployment

```bash
# Build
docker build -t home-device-bridge .

# Run
docker run -p 8000:8000 --env-file .env home-device-bridge
```

### Docker Compose

```bash
docker-compose up -d
```

## CI/CD

GitHub Actions builds the Docker image on every PR/push, and deploys to the home server on pushes to `main`.

Required repository secrets:
- `SERVER_HOST` (e.g. `192.168.1.111`)
- `SERVER_USER` (e.g. `vityuntu`)
- `SERVER_SSH_KEY` (private key with SSH access)
- `SERVER_DEPLOY_PATH` (e.g. `/home/vityuntu/homeserver/home-device-bridge`)
- `SERVER_PORT` (optional, defaults to 22)

Server prerequisites:
- `docker` + `docker compose` installed
- `.env` present at `SERVER_DEPLOY_PATH` (not overwritten by CI)
- Optional `config/devices.json` for device mapping (not overwritten by CI)

## Project Structure

```
home-device-bridge/
├── src/
│   └── server/
│       ├── mcp_server.py      # FastMCP server with tools
│       └── http_server.py     # HTTP/SSE transport wrapper
├── config/
│   └── devices.example.json   # Device configuration example
├── tests/                      # Test suite
├── .env.example               # Environment variables template
├── Dockerfile                 # Docker image
├── docker-compose.yml         # Docker Compose config
└── pyproject.toml             # Python project config
```

## Development

### Install dev dependencies

```bash
pip install -e ".[dev]"
```

### Run tests

```bash
pytest tests/ -v
```

### Code formatting

```bash
black .
ruff check .
```

## FastMCP Resources

- **Official FastMCP**: https://github.com/jlowin/fastmcp
- **MCP Documentation**: https://modelcontextprotocol.io
- **FastMCP Tutorial**: https://mcpcat.io/guides/building-mcp-server-python-fastmcp/

## Home Assistant Setup

1. Open Home Assistant
2. Go to Profile → Long-Lived Access Tokens
3. Create new token
4. Add token to `.env` file

## License

MIT License - see [LICENSE](LICENSE)

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Add tests
5. Submit pull request

## Support

Issues: https://github.com/victorduco/home-device-bridge/issues
