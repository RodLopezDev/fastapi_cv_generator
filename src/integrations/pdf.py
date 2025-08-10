"""
This module contains the integration with the PDF library.
"""

from weasyprint import HTML


def string_to_pdf(html_content: str, file_name: str) -> bool:
    """
    Convert a string to a PDF file
    """
    try:
        HTML(string=html_content).write_pdf(f"output/{file_name}.pdf")
        return True
    except Exception as e:
        return False
