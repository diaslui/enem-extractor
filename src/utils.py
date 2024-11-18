import re
import os

def parse_question_number(s: str) -> int:
    # extract real question number from string
    numbers = re.findall(r'\d+', s)
    return int(''.join(numbers))

def rename_file(image_output_path: str, f_name: str) -> None | str:
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