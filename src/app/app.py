"""
This module contains the main app for the API.
"""

from fastapi import FastAPI

from app.config import AppConfig

APP_VERSION = "1.0.0"


app = FastAPI(
    title="CV Generator",
    description="CV Generator",
    version=APP_VERSION,
    docs_url=None if AppConfig.PRODUCTION else "/docs",
    redoc_url=None if AppConfig.PRODUCTION else "/redoc",
)


@app.get("/", tags=["Health Check"])
async def health():
    """
    Get / app
    """
    return {
        "status": "ok",
        "version": APP_VERSION,
    }
