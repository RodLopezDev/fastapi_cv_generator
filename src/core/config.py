"""
This module contains the configuration for the application.
"""

import os

from dotenv import load_dotenv

load_dotenv(".env")


class AppConfig:
    """
    This class contains the configuration for the application.
    """

    PORT = int(os.getenv("PORT"))
    PRODUCTION = str(os.getenv("PRODUCTION")) == "true"
