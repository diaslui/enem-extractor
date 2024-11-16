import re
from .settings import MAX_QUESTIONS


def valid_question_number(s:str) -> bool:
    """
    This tests whether it is a valid question.
    It is a valid question if it has the term QUEST
    and the numbering from 0 to MAX_QUESTIONS next to it.

    Example:
    valid_question_number("questão 01")  # True

    :param s: str
    :return: bool
    
    """
    pattern = rf'\b(0?[0-9]|[1-8][0-9]|{MAX_QUESTIONS})\b'
    match = re.search(pattern, s)
    return match is not None

def extract_alternative(s:str) -> None | tuple:
    """
    This function checks if the string is an alternative to a question.

    To be a question, the text must start with an alternative
    and end with space.

    Examples:

    Agua mole pedra dura. -> None
    B  Agua mole pedra dura. -> ("B", "Agua mole pedra dura.")

    :param s: str
    :return: None | tuple
    """
    alternative = None
    alternatives = ["A", "B", "C", "D", "E"]

    for alternative in alternatives:
        if s.startswith(alternative):
            alternative = alternative
            break
    
    if alternative is None:
        return None
    
    if s.split(alternative)[1].startswith(" "):
        txt = s[s.index(alternative)+1:]
        txt = txt.lstrip()
        return (alternative, txt )
    
    return None