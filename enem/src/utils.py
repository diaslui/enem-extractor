import re
import os
from typing import Union
import sys
import colorama

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

def display_progress(startswith: str, actual: int, total: int) -> None:
    """
    This function is responsible for displaying the progress.

    :param startswith: str
    :param actual: int
    :param total: int
    :return: None
    """

    progress_str = f"\r{startswith} {actual}/{total}   " 
    
    sys.stdout.write(progress_str)
    sys.stdout.flush()

    if actual == total:
        sys.stdout.write("\n")

def display(message: str, color: str = '') -> None:
    """
    This function is responsible for displaying the message.

    :param message: str
    :param color: str
    :return: None
    """

    colors = {
        'red': colorama.Fore.RED,
        'green': colorama.Fore.GREEN,
        'yellow': colorama.Fore.YELLOW,
        'white': colorama.Fore.WHITE,
        'lightblue': colorama.Fore.LIGHTBLUE_EX,
        'lightblack': colorama.Fore.LIGHTBLACK_EX
    }

    if not color:
        print(message)
        return

    if color in colors:
        print(colors[color] + message)

def validate_image(image) -> bool:
    """
    This function is responsible for validating the image.

    :param image: Image
    :return: bool
    """

    MIN_WIDTH = 50
    MIN_HEIGHT = 50

    if image.width < MIN_WIDTH or image.height < MIN_HEIGHT:
        return False

    return True

def display_text_details(span):
    return {
        "font_style": get_font_style(span['font']),
        "font_color": convert_to_hex_color(span['color'], span['alpha']),
        "font_name": span["font"],
        "font_size": round(span["size"], 3),
    }