"""
This module contains the build API.
"""

from fastapi import APIRouter

from integrations.pdf import string_to_pdf
from modules.curriculum.dto import CurriculumDTO
from modules.template.service import get_html_content

router = APIRouter(tags=["Builder"])


@router.post("")
async def build(dto: CurriculumDTO):
    """
    Build a CV
    """
    html_content = get_html_content(dto)
    success = string_to_pdf(html_content, dto.metadata.identifier or "curriculum")

    if success:
        return {
            "message": "CV built successfully",
            "url": f"/v1/viewer/{dto.metadata.identifier}",
        }

    return {"message": "Error building CV"}
