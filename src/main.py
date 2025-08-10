"""
This module contains the main entry point for the application.
"""

from app.config import AppConfig


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.app:app",
        host="0.0.0.0",
        port=AppConfig.PORT,
        reload=not AppConfig.PRODUCTION,
        workers=1,
    )
