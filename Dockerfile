FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY pyproject.toml ./
RUN pip install --no-cache-dir -e .

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Run HTTP/SSE server
CMD ["python", "-m", "src.server.http_server"]
