"""
This module contains the main app for the API.
"""

from fastapi import FastAPI

from api.v1 import build, viewer
from core.config import AppConfig

APP_VERSION = "1.0.0"


app = FastAPI(
    title="CV Generator",
    description="CV Generator",
    version=APP_VERSION,
    docs_url=None if AppConfig.PRODUCTION else "/docs",
    redoc_url=None if AppConfig.PRODUCTION else "/redoc",
)


app.include_router(build.router, prefix="/v1/build")
app.include_router(viewer.router, prefix="/v1/viewer")


@app.get("/", tags=["Health Check"])
async def health():
    """
    Get / app
    """
    return {
        "status": "ok",
        "version": APP_VERSION,
    }
