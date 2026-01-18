# Home Device Bridge

MCP (Model Context Protocol) server for communication between home devices.

## Overview

Home Device Bridge is an MCP server that enables seamless communication and control between various home devices including Home Assistant, smartphones, and other IoT devices.

## Features

- 🏠 Home Assistant integration
- 📱 Mobile device notifications (iOS/Android)
- 🔔 Push notification management
- 🔗 Device-to-device communication
- 🛠️ RESTful API interface

## Architecture

```
home-device-bridge/
├── src/
│   ├── server/          # MCP server implementation
│   ├── integrations/    # Device integrations (Home Assistant, etc.)
│   ├── notifications/   # Notification handlers
│   └── utils/          # Helper utilities
├── config/             # Configuration files
├── tests/              # Test suite
└── docs/               # Documentation
```

## Prerequisites

- Python 3.11+
- Home Assistant instance
- API tokens for device integrations

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/home-device-bridge.git
cd home-device-bridge

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .
```

## Configuration

Create a `.env` file in the project root:

```env
# Home Assistant
HA_URL=http://homeassistant.local:8123
HA_TOKEN=your_token_here

# Server settings
MCP_HOST=0.0.0.0
MCP_PORT=8000
```

## Usage

```bash
# Start the MCP server
python -m src.server.main

# Run tests
pytest

# Development mode with auto-reload
python -m src.server.main --dev
```

## API Endpoints

### Health Check
```bash
GET /health
```

### Send Notification
```bash
POST /notify
Content-Type: application/json

{
  "device": "iphone_2",
  "title": "Notification Title",
  "message": "Notification message",
  "data": {}
}
```

### Get Devices
```bash
GET /devices
```

## Development

### Project Structure

- `src/server/` - MCP server core
- `src/integrations/` - Integration modules for different platforms
- `src/notifications/` - Notification service implementations
- `src/utils/` - Shared utilities and helpers
- `config/` - Configuration templates and schemas
- `tests/` - Unit and integration tests

### Running Tests

```bash
pytest tests/ -v
```

### Code Style

This project uses:
- `black` for code formatting
- `ruff` for linting
- `mypy` for type checking

```bash
# Format code
black .

# Lint
ruff check .

# Type check
mypy src/
```

## Deployment

### Docker

```bash
docker build -t home-device-bridge .
docker run -p 8000:8000 --env-file .env home-device-bridge
```

### Docker Compose

```bash
docker-compose up -d
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) for details

## Roadmap

- [ ] Home Assistant integration
- [ ] iOS push notifications
- [ ] Android push notifications
- [ ] Device state synchronization
- [ ] Automation triggers
- [ ] Web dashboard
- [ ] WebSocket support for real-time updates

## Support

For issues and questions, please use the [GitHub Issues](https://github.com/YOUR_USERNAME/home-device-bridge/issues) page.
