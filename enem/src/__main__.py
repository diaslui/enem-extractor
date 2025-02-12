import fitz
import colorama
import io
import os
from PIL import Image
from typing import Union, Optional
from .validations import valid_question_number
from .utils import parse_question_number, rename_file, get_font_style, convert_to_hex_color
from .answers import answer_parser, test_correction
from .image_extractor import resolve_image
from .validations import is_question_alternative
from .settings import QUESTION_RANGE, DAY_SPLIT

"""

(c) 2024 Pedro L. Dias
https://github.com/diaslui/enem-extractor/

------------------------------------------------------------------

This code consider 2 days for test aplication
Day 1 -> Linguagens, Códigos e suas Tecnologias
Day 2 -> Ciências da Natureza e suas Tecnologias + Matemática e suas Tecnologias
"""

def extractor(file_pdf_path: str, root_path: str, test_answer_key_path: Optional[str] = None) -> Optional[tuple]:
    """
    This function is the main function of the application.

    :param file_pdf_path: str path pdf file
    :param root_path: str path to root path
    :param test_answer_key_path: str path to pdf file
    :return: dict or None

    """
    test_answer: Optional[dict] = {} if test_answer_key_path else None

    if test_answer_key_path is not None and test_answer != None:
        test_answer = answer_parser(test_answer_key_path)

    day: int | None = None
    questions: list  = []
    img_data: list = []
    doc = fitz.open(file_pdf_path)
    file_name = os.path.splitext(os.path.basename(file_pdf_path))[0]
    actual_question: Optional[dict] = None
    question_content: list = []
    question_alternatives: dict = {}
    root_path = os.path.join(root_path, f"output_{file_name}")
    if not os.path.exists(os.path.join(root_path, "img")):
        os.makedirs(os.path.join(root_path, "img"))
    image_output_path = os.path.join(root_path, "img")

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
                    #    print(f"Text: {text.strip()}")

                        if "questão" in text.lower() and valid_question_number(text):
                            # question found
                            actual_question = parse_question_number(text)
                            question_content = []

                            if day is None and isinstance(DAY_SPLIT, int) and DAY_SPLIT > 0 and isinstance(actual_question, int):
                                if actual_question > DAY_SPLIT and actual_question <= QUESTION_RANGE[1]:
                                    print(colorama.Fore.LIGHTBLACK_EX + f"Identified as day 2")
                                    day = 2
                                elif actual_question <= DAY_SPLIT and isinstance(QUESTION_RANGE, (list, tuple)) and actual_question >= QUESTION_RANGE[0]:
                                    print(colorama.Fore.LIGHTBLACK_EX + f"Identified as day 1")
                                    day = 1
                                
                            continue

                        alternative_test = is_question_alternative(text)

                        if alternative_test != None and question_content != []:
                            # alternative found (A, B, C, D, E)..
                            alternative = alternative_test

                            if question_alternatives == {} and alternative != 0:
                                # fake call!!
                                # if there is no alternative A, there is no point in having alternative C.
                                continue
                            if alternative != 0:
                                old_alternative = question_alternatives.get(alternative-1)

                                if not old_alternative:
                                    continue

                            question_alternatives[alternative] = {
                                "alternative": text.strip(),
                                "content": [],
                                "type": "",
                                "alternative_value": alternative,
                                "correct": False
                            }
                            continue

                        if alternative_test == None and len(text.strip()) < 2:
                            # empty line found
                            continue

                        if alternative_test == None and question_alternatives != {}:
                            # alternative text found
                            question_alternatives[len(question_alternatives)-1]["content"].append({
                                "font_style": get_font_style(span['font']),
                                "font_color": convert_to_hex_color(span['color'], span['alpha']),
                                "font_name": span["font"],
                                "font_size": round(span["size"], 3),
                                "type": "text",
                                "content": text
                            })

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
                                "font_style": get_font_style(span['font']),
                                "font_color": convert_to_hex_color(span['color'], span['alpha']),
                                "font_name": span["font"],
                                "font_size": round(span["size"], 3),
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

    if test_answer and test_answer != None:
        print(colorama.Fore.WHITE + "Starting correction...")
        print(test_answer)
        questions = test_correction(questions, test_answer)
    return (root_path, questions) if questions else None
