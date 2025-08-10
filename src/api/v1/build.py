"""
This module contains the build API.
"""

from fastapi import APIRouter

router = APIRouter(tags=["Builder"])


@router.post("")
async def build():
    """
    Build a CV
    """
    return {"message": "CV built successfully"}
