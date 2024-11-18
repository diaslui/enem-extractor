from src.index import extractor
import os
import json
import time

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

extraction = extractor(file_pdf_path="2024.pdf", root_path=os.path.join(os.getcwd()), test_answer_key_path="2024_g.pdf")
if extraction:
    assets, result = extraction
    if result:
        json_path = os.path.join(assets, "output.json")
        with open(json_path, "w", encoding="utf-8") as f:
            f.write(json.dumps({"data":result}, indent=4, ensure_ascii=False))
else:
    print("Extraction failed, received None")