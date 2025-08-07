# Simple FastAPI Service

A simple FastAPI service with health and echo endpoints.

## Features

- **Health Check Endpoint**: `/health` - Returns service status
- **Echo Endpoints**: 
  - POST `/echo` - Echo message from request body
  - GET `/echo/{message}` - Echo message from URL path
- **Root Endpoint**: `/` - Service information

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Service

### Using Python directly:
```bash
python main.py
```

### Using Uvicorn:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The service will be available at `http://localhost:8000`

## API Documentation

Once the service is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Example Usage

### Health Check
```bash
curl http://localhost:8000/health
```

Response:
```json
{
  "status": "healthy",
  "message": "Service is running properly"
}
```

### Echo (POST)
```bash
curl -X POST "http://localhost:8000/echo" \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello World!"}'
```

Response:
```json
{
  "echo": "Hello World!"
}
```

### Echo (GET)
```bash
curl http://localhost:8000/echo/Hello%20World
```

Response:
```json
{
  "echo": "Hello World"
}
```
