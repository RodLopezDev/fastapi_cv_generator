"""
This module contains the DTOs for the curriculum.
"""

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field


class HTMLProps(BaseModel):
    margin_bottom: int = Field(default=0)


class Laguage(StrEnum):
    """
    Language Enum
    """

    ES = "es"
    EN = "en"


class PersonalInfoDTO(BaseModel):
    """
    Personal Info DTO
    """

    name: str
    email: str
    phone: str
    github: str
    linkedin: str
    resume: str


class MetadataDTO(BaseModel):
    """
    Metadata DTO
    """

    language: Laguage = Field(default=Laguage.EN)
    identifier: Optional[str] = None


class ExperienceDTO(BaseModel):
    """
    Experience DTO
    """

    position: str
    company: str
    year_start: str
    year_end: str
    descriptions: list[str] = Field(default_factory=list)
    stack: list[str] = Field(default_factory=list)
    html_props: Optional[HTMLProps] = None


class ProjectDTO(BaseModel):
    """
    Project DTO
    """

    name: str
    link: str
    description: str


class EducationDTO(BaseModel):
    """
    Education DTO
    """

    name: str
    mode: str
    university: str
    year_start: str
    year_end: str


class CurriculumDTO(BaseModel):
    """
    Curriculum DTO
    """

    metadata: MetadataDTO
    personal_info: PersonalInfoDTO
    experiences: list[ExperienceDTO] = Field(default_factory=list)
    projects: list[ProjectDTO] = Field(default_factory=list)
    education: list[EducationDTO] = Field(default_factory=list)
