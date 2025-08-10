"""
This module contains the service for the templates.
"""

from jinja2 import Environment, FileSystemLoader

from modules.curriculum.dto import CurriculumDTO, Laguage


def get_html_content(dto: CurriculumDTO) -> str:
    """
    Get the HTML content of a template
    """

    metadata_es = {
        "title_experience": "Experiencia",
        "title_projects": "Proyectos",
        "title_education": "Educación",
    }

    metadata_en = {
        "title_experience": "Experience",
        "title_projects": "Projects",
        "title_education": "Education",
    }

    data = {
        "metadata": metadata_en if dto.metadata.language == Laguage.EN else metadata_es,
        "name": dto.personal_info.name,
        "email": dto.personal_info.email,
        "phone": dto.personal_info.phone,
        "github": dto.personal_info.github,
        "linkedin": dto.personal_info.linkedin,
        "experiences": dto.experiences,
        "projects": dto.projects,
        "education": dto.education,
    }

    env = Environment(loader=FileSystemLoader("src/modules/template/templates/base"))
    template = env.get_template("index.html")
    html_content = template.render(data)

    css_content = open(
        file="src/modules/template/templates/base/index.css",
        mode="r",
        encoding="utf-8",
    ).read()

    html_content = html_content.replace(
        '<link rel="stylesheet" href="index.css">', f"<style>{css_content}</style>"
    )

    return html_content
