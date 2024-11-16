import fitz
from .validations import valid_question_number
from .utils import parse_question_number
from .answers import answer_parser
"""
This code consider 2 days for test aplication
Day 1 -> Linguagens, Códigos e suas Tecnologias
Day 2 -> Ciências da Natureza e suas Tecnologias + Matemática e suas Tecnologias
"""

def extractor(file_pdf_path:str, test_answer_key_path: str | None=None) -> dict | None:
    """
    This function is the main function of the application.

    :param file_pdf_path: str path pdf file
    :param test_answer_key_path: str path to pdf file
    :return: dict or None

    """
    test_answer: dict | None = {} if test_answer_key_path else None
    schema: dict = {}

    if test_answer:
        test_answer = answer_parser(test_answer_key_path)

#    with fitz.open(file_pdf_path) as pdf:
#



    
    return schema if schema else None
