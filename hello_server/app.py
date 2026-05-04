"""FastAPI application for the hello server."""

from fastapi import FastAPI

app = FastAPI(title="Hello Server")


@app.get("/hello")
def hello() -> str:
    """Return the hello response."""
    return "world"

