import re
import os
from typing import Union

def parse_question_number(s: str) -> int:
    # extract real question number from string
    numbers = re.findall(r'\d+', s)
    return int(''.join(numbers))

def rename_file(image_output_path: str, f_name: str) -> Union[None, str]:
    """
    This function is responsible for renaming the file.

    :param image_output_path: str file path
    :param f_name: name to rename
    :return: None
    """
    try:
        img_dir = os.path.dirname(image_output_path)
        file_extension = image_output_path.split('.')[-1]
        new_file_path = os.path.join(img_dir, f"{f_name}.{file_extension}")
        counter = 1
        while os.path.exists(new_file_path):
            new_file_path = os.path.join(img_dir, f"{f_name}_{counter}.{file_extension}")
            counter += 1
        os.rename(image_output_path, new_file_path)
        return new_file_path
    except Exception as e:
        return None
    
def get_font_style(font: str) -> str:
    """
    This function is responsible for extracting the font style.

    :param font: str
    :return: str
    """

    font = font.lower()
    
    if 'bold' in font:
        return "bold"
    if 'italic' in font:
        return "italic"
    if 'black' in font:
        return "black"
    
    return "regular"

def convert_to_hex_color(color: int, alpha: int = 255) -> str:
    """
    This function is responsible for converting the color to hexadecimal.

    :param color: int
    :param alpha: int
    :return: str
    """
    
    r = (color >> 16) & 0xFF  # red
    g = (color >> 8) & 0xFF   # green
    b = color & 0xFF          # blue

    return f'#{r:02X}{g:02X}{b:02X}'