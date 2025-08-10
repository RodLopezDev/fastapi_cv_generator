"""
This module contains the viewer API.
"""

from fastapi import APIRouter

router = APIRouter(tags=["Viewer"])


@router.get("/{cv_id}")
async def get_cv(cv_id: str):
    """
    Get a CV
    """
    return {"message": "CV built successfully"}
