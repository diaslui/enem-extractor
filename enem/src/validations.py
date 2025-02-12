import re
from .settings import QUESTION_RANGE
from typing import Optional

def valid_question_number(s:str) -> bool:
    """
    This tests whether it is a valid question.
    It is a valid question if it has the term QUEST
    and the numbering from 0 to MAX_QUESTION_NUMBER next to it.

    Example:
    valid_question_number("questão 01")  # True
    valid_question_number("questão 181")  # False
    valid_question_number("questão 97")  # True

    :param s: str
    :return: bool
    
    """
    match = re.search(r'\b(\d+)\b', s)

    if not match:
        return False
    
    question_number = int(match.group(1))

    if QUESTION_RANGE[0] <= question_number <= QUESTION_RANGE[1]:
        return True
    
    return False

def is_question_alternative(s:str) -> Optional[int]:
    """
    This function checks if the string is an alternative to a question.

    To be a question, the text must start with an alternative.

    :param s: str
    :return: None | int (index of alternative)
    """
    alternatives = ["A", "B", "C", "D", "E"]
    s = s.strip()

    if s in alternatives:
        return alternatives.index(s)
    
    return None