from src.index import extractor
import os

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

extractor(file_pdf_path="2024.pdf", root_path=os.path.join(os.getcwd()))