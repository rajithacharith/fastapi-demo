from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

app = FastAPI(
    title="Simple FastAPI Service",
    description="A simple FastAPI service with health and echo endpoints",
    version="1.0.0"
)


class EchoRequest(BaseModel):
    message: str


class EchoResponse(BaseModel):
    echo: str


class HealthResponse(BaseModel):
    status: str
    message: str


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint to verify service is running"""
    return HealthResponse(
        status="healthy",
        message="Service is running properly"
    )


@app.post("/echo", response_model=EchoResponse)
async def echo_message(request: EchoRequest):
    """Echo endpoint that returns the received message"""
    return EchoResponse(echo=request.message)


@app.get("/echo/{message}", response_model=EchoResponse)
async def echo_message_get(message: str):
    """Echo endpoint that returns the message from URL path"""
    return EchoResponse(echo=message)


@app.get("/")
async def root():
    """Root endpoint with basic service information"""
    return {
        "service": "Simple FastAPI Service",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "echo_post": "/echo",
            "echo_get": "/echo/{message}"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
