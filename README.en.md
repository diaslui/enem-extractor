
# Enem Extractor

[![pt-br](https://img.shields.io/badge/lang-ptbr-red.svg)](https://github.com/diaslui/enem-extractor/blob/main/readme.md)
<a href="https://pypi.python.org/pypi/enem" target="_blank"><img src="https://img.shields.io/pypi/v/enem.svg?color=3399EE" alt="PyPI version" /></a>

[Versão em Português](https://github.com/diaslui/enem-extractor/blob/main/readme.en.md)

> ⭐ Star this project to support!



## What is ENEM?

The National High School Exam (ENEM) is a test created by the Brazilian Ministry of Education (MEC) that evaluates the quality of high school education in Brazil. It is also used as an entrance exam for many universities in the country.



**Enem Extractor** is a tool that automatically extracts questions from ENEM exams (or similar exams) and converts them into formats like JSON.

🏓 [See a real-world exam extracted by Enem Extractor here](https://diaslui.github.io/enem-extractor/)


## 🚀 Running

> To run this project, you need to have Python and pip installed. [You can download Python here](https://www.python.org/downloads/).

### 1. Install Enem Extractor

> To run **Enem Extractor** via `pip`, execute the following command in the terminal:

```bash
pip install enem
```

### 2. Extract an exam

After installation, you can extract questions from a PDF exam. Assuming you have an ENEM exam file named `test.pdf` in the same directory, just run:

```bash
enem test.pdf
```

The script will analyze the exam and extract the questions, generating a folder with an output JSON file containing the extracted data and other exam assets. [See more details about the command output here](#output).

### 3. Additional parameters

You can provide additional parameters to customize the extraction process:

- `-f` or `--file`: Path to the PDF exam file. (mandatory)
- `g` or `-key`: Path to the PDF answer key file. (optional)
- `-o` or `--output`: Path where the folder with the extracted files will be created. (optional)

Example of usage with parameters:

```bash
enem -f test.pdf -g key.pdf -o C:\documents
```

This command will extract the questions from the `test.pdf` exam, correct them with the `keya.pdf` answer key, and save the results folder in `C:\documents`.

## Output

**[Learn about the extraction outputs by clicking here.](examples/output_example/readme.md)**

<img src="https://github.com/user-attachments/assets/9e78b4f0-2055-4f32-a9c5-1bc3e96a2fdc" alt="demo_enem" width="350"/>

## 🔧 How to Contribute

1. Fork this repository.
2. Create a branch for your modification (`git checkout -b feature/new-feature`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the original repository (`git push origin feature/new-feature`).
5. Create a new Pull Request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Useful Links

- [PyMuPDF Documentation](https://pypi.org/project/PyMuPDF/)
- [Repository](https://github.com/diaslui/enem-extractor)
- [English version of README](https://github.com/diaslui/enem-extractor/blob/main/readme.en.md)

---

### 📢 Issues

If you have any questions, want to suggest improvements, or find issues, feel free to [open an issue](https://github.com/diaslui/enem-extractor/issues).

### 🌀 Subdependencies

- [PyMuPDF](https://pypi.org/project/PyMuPDF/) - PDF parsing
- [Pillow](https://pypi.org/project/Pillow/) - Image processing
- [Colorama](https://pypi.org/project/colorama/) - Terminal colors

Created with ❤️ by [Pedro L. Dias](https://github.com/diaslui)

