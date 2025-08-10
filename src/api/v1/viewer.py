"""
This module contains the viewer API.
"""

import os

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(tags=["Viewer"])


@router.get("/{cv_id}")
async def get_pdf(cv_id: str):
    """
    Muestra el PDF generado
    """
    pdf_path = os.path.abspath(f"output/{cv_id}.pdf")
    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="curriculum.pdf",
        headers={"Content-Disposition": f"inline; filename=curriculum.pdf"},
    )
