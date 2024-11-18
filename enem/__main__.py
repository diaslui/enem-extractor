import os
import sys
from .src.__main__ import extractor
import json
import time
import colorama
from argparse import ArgumentParser
import sys

colorama.init(autoreset=True)

"""
(c) 2024 Pedro L. Dias
Licensed under the MIT License
https://github.com/luiisp/enem-extractor

------------------------------------------------------------------
Important notice:

This code was made using models from Enem 2024,
it is compatible with the model adopted since 2017,
some tests from previous years may have difficulty or not work.
"""

def main():
    if len(sys.argv) <= 1:
        print(colorama.Fore.RED + "No arguments provided.")
        print(colorama.Fore.YELLOW + "Usage: enem -f <file_path> [-k <key_path>] [-o <output_path>]")
        sys.exit(1)
    parser = ArgumentParser(
        description="CLI Tool for ENEM PDF Extraction and JSON Export."
    )
    parser.add_argument(
        "-f", "--file", required=False, help="Path to the input PDF file."
    )
    parser.add_argument(
        "-k", "--key", required=False, help="Path to the test answer key PDF file."
    )
    parser.add_argument(
        "-o", "--output", required=False, help="Path to save the output JSON file."
    )

    args, positional_args = parser.parse_known_args()

    file_path = args.file or (positional_args[0] if len(positional_args) > 0 else None)
    key_path = args.key or (positional_args[1] if len(positional_args) > 1 else None)
    output_path = args.output or (positional_args[2] if len(positional_args) > 2 else os.getcwd())

    if not file_path:
        print(colorama.Fore.RED + "Error: No input file provided.")
        print(colorama.Fore.YELLOW + "Usage: enem -f <file_path> [-k <key_path>] [-o <output_path>]")
        sys.exit(1)

    if not os.path.exists(file_path):
        print(colorama.Fore.RED + f"Error: File not found: {file_path}")
        sys.exit(1)

    if key_path and not os.path.exists(key_path):
        print(colorama.Fore.RED + f"Error: Answer key file not found: {key_path}")
        sys.exit(1)

    if output_path and not os.path.isdir(os.path.dirname(output_path)):
        print(colorama.Fore.RED + f"Error: Output directory does not exist: {os.path.dirname(output_path)}")
        sys.exit(1)

    print(colorama.Fore.WHITE + "Starting extraction...")
    start_time = time.time()

    try:
        extraction = extractor(
            file_pdf_path=file_path,
            root_path=os.getcwd(),
            test_answer_key_path=key_path,
        )

        if extraction:
            output_path, result = extraction
            if result:
                output_file = output_path if output_path.endswith(".json") else os.path.join(output_path, "output.json")
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump({"data": result}, f, indent=4, ensure_ascii=False)

                elapsed_time = time.time() - start_time
                print(colorama.Fore.GREEN + f"Extraction completed successfully.")
                print(colorama.Fore.WHITE + f"{len(result)} questions extracted in {elapsed_time:.2f} seconds.")
                print(colorama.Fore.LIGHTBLUE_EX + f"Output file saved at: {output_file}")
        else:
            print(colorama.Fore.RED + "Error: Extraction failed. No data returned.")
    except Exception as e:
        print(colorama.Fore.RED + f"An error occurred during extraction: {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()