import fitz
import io
import os
from PIL import Image
from typing import Union, Optional
from .validations import valid_question_number
from .utils import parse_question_number, rename_file
from .answers import answer_parser
from .image_extractor import resolve_image
from .validations import is_question_alternative

"""

(c) 2024 Pedro L. Dias
https://github.com/luiisp/enem-extractor/

------------------------------------------------------------------

This code consider 2 days for test aplication
Day 1 -> Linguagens, Códigos e suas Tecnologias
Day 2 -> Ciências da Natureza e suas Tecnologias + Matemática e suas Tecnologias
"""

def extractor(file_pdf_path:str, root_path:str, test_answer_key_path: str | None=None) -> list | None:
    """
    This function is the main function of the application.

    :param file_pdf_path: str path pdf file
    :param root_path: str path to root path
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
    if not os.path.exists(os.path.join(root_path, "img")):
        os.makedirs(os.path.join(root_path, "img"))
    image_output_path = os.path.join(root_path, "img")
    print("Image output path: ", image_output_path)
    for page_num, page in enumerate(doc, start=1):
        images = page.get_images(full=True)
        for img in images:
            img_ = resolve_image(image_output_path=image_output_path, page=page ,doc=doc, img=img)
            if img_:
                img_data.append(img_)

        for block in page.get_text("dict")["blocks"]:
            block_type = block["type"]
            if block_type == 0: # text
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"]

                        if "questão" in text.lower() and valid_question_number(text):
                            # question found
                            actual_question = parse_question_number(text)
                            question_content = []
                            continue

                        alternative_test = is_question_alternative(text)

                        if alternative_test != None and question_content != []:
                            # alternative found (A, B, C, D, E)..
                            alternative = alternative_test
                            question_alternatives[alternative] = {
                                "text": "",
                                "alternative_value": alternative,
                                "correct": False
                            }
                            continue

                        if alternative_test == None and len(text.strip()) < 2:
                            # empty line found
                            continue

                        if alternative_test == None and question_alternatives != {}:
                            # alternative text found
                            question_alternatives[len(question_alternatives)-1]["text"] += text
                            if question_alternatives[len(question_alternatives)-1]["alternative_value"] == 4:
                                # EOQ end of question
                                questions.append({
                                        "number": actual_question,
                                        "content": question_content,
                                        "alternatives": question_alternatives
                                })
                                actual_question = None
                                question_content = []
                                question_alternatives = {}
                            continue

                        if actual_question:
                            # question content (text) found
                            question_content.append({
                                "type": "text",
                                "content": text
                            })
                        continue

            if block_type == 1: # image
                if actual_question is None:
                    continue

                image = Image.open(io.BytesIO(block["image"]))
                width, height = image.size

                for data in img_data:
                    if data["width"] == width and data["height"] == height:
                        img_data.remove(data)
                        new_path = rename_file(data["imagePath"], f"question-{actual_question}")
                        if new_path:
                            question_content.append({
                                    "type": "image",
                                    "content": new_path if new_path else data["imagePath"]
                                })

                        break
    
    if img_data.__len__() > 0:
        for data in img_data:
            os.remove(data["imagePath"])

    return questions if questions else None
