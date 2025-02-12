import re
import fitz
from .validations import is_question_alternative
from typing import Union

def answer_parser(file_pdf_src: str) -> Union[dict, None]:
    """
    This function is responsible for extracting the answers from the test key.

    Based on recent template models: https://download.inep.gov.br/enem/provas_e_gabaritos/2023_GB_impresso_D1_CD1.pdf
    100% in tests since 2017.
    
    consider _ for questions of es language in answers

    :param pdf_file_src: str
    :return: dict
    """
    
    answers:dict = {}
    with fitz.open(file_pdf_src) as pdf:
        for page_num, page in enumerate(pdf, start=1):

            text = page.get_text("text")
            lines = text.split("\n")

            q_n = None
            for line in lines:
                if len(line) > 3 or not line.strip() or line == " ":
                    continue

                if re.match(r'^\s*\d+\s*$', line):
                    q_n = int(line)
                    continue

                if q_n is not None:
                    if answers.get(q_n):
                        if str(q_n)+"_1" in answers:
                            answers[str(q_n)+"_1"] += line
                        else:
                            answers[str(q_n)+"_1"] = line
                    else:
                        answers[q_n] = line
                    continue   

          
    return answers if answers else None


def test_correction(questions:list, answers:dict) -> list:
    """
    This function is responsible for correcting the test based on the answers extracted from the test key.

    :param questions: list
    :param answers: dict
    :return: dict
    """
    for answer in answers.items():
        q_number = answer[0]
        q_answer = answer[1]

        alt = is_question_alternative(q_answer)

        if alt == None:
            continue

        for question in questions:
            if q_number == question['number'] or q_number == f"{question['number']}_1": 
                if any(alt.get("correct") for alt in question['alternatives'].values()):
                   continue
                for alternative in question['alternatives'].items():
                    if alternative[1]['alternative_value'] == alt:
                        alternative[1]["correct"] = True
                        break

    return questions
        

        