import fitz
from typing import Union, Optional
from .validations import valid_question_number
from .utils import parse_question_number
from .answers import answer_parser
from .image_extractor import resolve_image
"""

(c) 2024 Pedro L. Dias
https://github.com/luiisp/enem-extractor/

------------------------------------------------------------------

This code consider 2 days for test aplication
Day 1 -> Linguagens, Códigos e suas Tecnologias
Day 2 -> Ciências da Natureza e suas Tecnologias + Matemática e suas Tecnologias
"""

def extractor(file_pdf_path:str, test_answer_key_path: str | None=None) -> list | None:
    """
    This function is the main function of the application.

    :param file_pdf_path: str path pdf file
    :param test_answer_key_path: str path to pdf file
    :return: dict or None

    """
    test_answer: dict | None = {} if test_answer_key_path else None

    if test_answer:
        test_answer = answer_parser(test_answer_key_path)

    questions: list  = []
    img_data: list = []
    doc = fitz.open(file_pdf_path)
    actual_question: dict | None = None
    question_content: list = []
    question_alternatives: dict = {}
    for page_num, page in enumerate(doc, start=1):
        images = page.get_images(full=True)
        for img in images:
            img_ = resolve_image(image_output_path="images", page=page ,doc=doc, img=img)
            if img_:
                img_data.append(img_)





    
    return questions if questions else None
