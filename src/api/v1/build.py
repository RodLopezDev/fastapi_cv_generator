"""
This module contains the build API.
"""

from fastapi import APIRouter
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

router = APIRouter(tags=["Builder"])


@router.post("")
async def build():
    """
    Build a CV
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
        "metadata": metadata_en,
        "name": "Rodrigo López",
        "email": "rodrigolopezdev@gmail.com",
        "phone": "+51 984645581",
        "github": "https://github.com/RodLopezDev",
        "linkedin": "https://www.linkedin.com/in/rodrigo-lopez-rojas",
        "experiences": [
            {
                "position": "Software Engineer (Short Term Project)",
                "company": "IIAP",
                "year_start": "FEB 2025",
                "year_end": "Actualidad",
                "descriptions": [
                    "Desarrollo de app mobile para detección y conteo de alevines en un entorno controlado.",
                    "Desarrollo de arquitectura backend para administración de app mobile y para ingesta de información a servicio cloud.",
                ],
                "stack": [
                    "Python",
                    "FastAPI",
                    "React Native",
                    "React",
                    "Docker",
                    "AWS",
                    "Git",
                    "GitHub",
                ],
            }
        ],
        "projects": [
            {
                "name": "Web Personal",
                "link": "https://rodrigolopez.dev",
                "description": "Sitio web personal con blog y portafolio de proyectos, desarrollado con NextJS 15, FastAPI 0.115.8 y Mongo 6.0, desplegado en Vercel y Digital Ocean.",
            },
            {
                "name": "@rodlopez/clean-code",
                "link": "https://www.npmjs.com/package/@rodlopez/clean-code",
                "description": "Toolkit para manejo de codigo clean en ReactJS, orientado a mejor manejo del estado y repositories.",
            },
        ],
        "education": [
            {
                "name": "Ingles",
                "mode": "Remote",
                "university": "EF English",
                "year_start": "Feb 2025",
                "year_end": "Actualidad",
            },
            {
                "name": "Maestría en Gestión de la Tecnologías de Información e Ingeniería del Software",
                "mode": "Iquitos, Perú",
                "university": "Universidad Nacional de la Amazonía Peruana - Escuela de Postgrado",
                "year_start": "Nov 2017",
                "year_end": "En pausa",
            },
            {
                "name": "Bachiller en Ingeniería de Sistemas e Informática",
                "mode": "Iquitos, Perú",
                "university": "Universidad Nacional de la Amazonía Peruana",
                "year_start": "Mar 2012",
                "year_end": "Dic 2016",
            },
        ],
    }

    env = Environment(loader=FileSystemLoader("src/templates/base"))
    template = env.get_template("index.html")
    html_content = template.render(data)

    css_content = open(
        file="src/templates/base/index.css", mode="r", encoding="utf-8"
    ).read()

    html_content = html_content.replace(
        '<link rel="stylesheet" href="index.css">', f"<style>{css_content}</style>"
    )

    HTML(string=html_content, base_url="../").write_pdf("output/curriculum.pdf")

    return {"message": "CV built successfully"}
