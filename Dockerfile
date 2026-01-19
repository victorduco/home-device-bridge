FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir .

# Expose port
EXPOSE 8000

# Run FastMCP server (HTTP transport)
CMD ["python", "-m", "src.server.mcp_server"]
