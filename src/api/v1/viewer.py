"""
This module contains the viewer API.
"""

import os

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(tags=["Viewer"])


@router.get("")
async def get_all():
    """
    Descarga el PDF generado
    """
    pdf_files = [f for f in os.listdir("output") if f.endswith(".pdf")]
    return [
        {"name": f.replace(".pdf", ""), "url": f"/v1/viewer/cv/{f}"} for f in pdf_files
    ]


@router.get("/cv/{cv_id}")
async def get_pdf(cv_id: str):
    """
    Muestra el PDF generado
    """
    pdf_path = os.path.abspath(f"output/{cv_id}.pdf")
    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="curriculum.pdf",
        headers={"Content-Disposition": f"inline; filename={cv_id}.pdf"},
    )
