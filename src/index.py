import fitz
from .validations import valid_question_number
from .utils import parse_question_number
"""
This code consider 2 days for test aplication
Day 1 -> Linguagens, Códigos e suas Tecnologias
Day 2 -> Ciências da Natureza e suas Tecnologias + Matemática e suas Tecnologias
"""

def extractor(file_pdf, test_answer_key=None) -> dict | None:
    """
    This function is the main function of the application.

    :param file_pdf: pdf file
    :param test_answer_key: pdf file 
    :return: dict or None

    """
    day_1 = False
    schema = {}

    
    return schema if schema else None
