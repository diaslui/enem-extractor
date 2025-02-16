import os
import sys
from .src.__main__ import extractor
import json
import time
import colorama
from argparse import ArgumentParser
from .src.utils import display
from .src.settings import CREDITS, VERSION
import sys

colorama.init(autoreset=True)

"""
(c) 2024 Pedro L. Dias
Licensed under the MIT License
https://github.com/diaslui/enem-extractor

------------------------------------------------------------------
Important notice:

This code was made using models from Enem 2024,
it is compatible with the model adopted since 2017,
some tests from previous years may have difficulty or not work.
"""

def main():
    if len(sys.argv) <= 1:
        display("No arguments provided.", 'red')
        display("Usage: enem -f <file_path> [-g <key_path>] [-o <output_path>]", 'yellow')
        sys.exit(1)
    parser = ArgumentParser(
        description="CLI Tool for ENEM PDF Extraction and JSON Export."
    )
    parser.add_argument(
        "-f", "--file", required=False, help="Path to the input PDF file."
    )
    parser.add_argument(
        "-g", "--key", required=False, help="Path to the test answer key PDF file."
    )
    parser.add_argument(
        "-o", "--output", required=False, help="Path to save the output JSON file."
    )
    parser.add_argument(
        '-m', '--minimal', required=False, help='Minimal output (only questions and answers).'
    )

    parser.add_argument('-v', '--version', action='version', version=f'{VERSION}')
    parser.add_argument('-c', '--credits', action='store_true', help='Show credits and license information.')

    args, positional_args = parser.parse_known_args()

    if args.credits:
        display(CREDITS, "yellow")
        sys.exit(0)

    file_path = args.file or (positional_args[0] if len(positional_args) > 0 else None)
    key_path = args.key or (positional_args[1] if len(positional_args) > 1 else None)
    output_path = args.output or (positional_args[2] if len(positional_args) > 2 else os.getcwd())
    minimal = args.minimal or False

    if not file_path:
        display("Error: No input file provided.", 'red')
        display("Usage: enem -f <file_path> [-g <key_path>] [-o <output_path>]", 'yellow')
        sys.exit(1)

    if not os.path.exists(file_path):
        display(f"Error: Input file not found: {file_path}", 'red')
        display("Usage: enem -f <file_path> [-g <key_path>] [-o <output_path]", 'yellow')
        sys.exit(1)

    if key_path and not os.path.exists(key_path):
        display(f"Error: Answer key file not found: {key_path}", 'red')
        sys.exit(1)

    if output_path and not os.path.isdir(os.path.dirname(output_path)):
        display(f"Error: Output directory not found: {output_path}", 'red')
        sys.exit(1)

    if minimal:
        display("Minimal output enabled. \n Content will be displayed in as few lines as possible.", 'yellow')

    display(f"Starting extraction from file: {file_path}", 'green')
    start_time = time.time()

    try:
        extraction = extractor(
            file_pdf_path=file_path,
            root_path=output_path,
            test_answer_key_path=key_path,
            minimal=minimal
        )

        if extraction:
            output_path, result = extraction
            if result:
                output_file = output_path if output_path.endswith(".json") else os.path.join(output_path, "output.json")
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump({"data": result}, f, indent=4, ensure_ascii=False)

                elapsed_time = time.time() - start_time
                display("Extraction completed successfully.", 'green')
                display(f"{len(result)} questions extracted in {elapsed_time:.2f} seconds.")
                display(f"Output saved to: {output_file}", 'lightblue')

        else:
            display("An error occurred during extraction.", 'red')
    except Exception as e:
        display(f"An error occurred during extraction: {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()