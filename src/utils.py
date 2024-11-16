import re

def parse_question_number(s: str) -> int:
    # extract real question number from string
    numbers = re.findall(r'\d+', s)
    return int(''.join(numbers))