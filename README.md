
<p align="center">
  <a href="https://github.com/diaslui/enem-extractor">
    <img loading="lazy" alt="enem-extractor" src="https://raw.githubusercontent.com/diaslui/enem-extractor/refs/heads/master/docs/assets/enem-extrac-banner.png" width="100%"/>
  </a>
</p>


# Enem Extractor


[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/diaslui/enem-extractor/blob/master/README.en.md)
<a href="https://pypi.python.org/pypi/enem" target="_blank"><img src="https://img.shields.io/pypi/v/enem.svg?color=3399EE" alt="PyPI version" /></a>
[![Downloads](https://pepy.tech/badge/enem)](https://pepy.tech/project/enem)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/enem)](https://pypi.org/project/enem/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/diaslui/enem-extractor/blob/master/LICENSE)
[![Issues](https://img.shields.io/github/issues/diaslui/enem-extractor.svg)](https://github.com/diaslui/enem-extractor/issues)




 [English version](https://github.com/diaslui/enem-extractor/blob/master/README.en.md)


> ⭐ Star this project to support!

**Enem Extractor** é uma ferramenta CLI que extrai/corrige questões de provas do ENEM e as converte em JSON mantendo assets (imagens, gráficos, etc.)

🏓 [Veja uma prova extraida pelo Enem Extractor no mundo real aqui](https://diaslui.github.io/enem-extractor/)

## 🗝️ Provas Extraídas

Neste repositório você pode encontrar todas as provas do **Enem** em **JSON** extraídas pelo Enem Extractor. [Clique aqui para ver](https://github.com/diaslui/enem-extractor/tree/master/provas).


## 🎯 Aplicações

- **Machine Learning**: Treine modelos de IA com questões do ENEM.

- **Web Apps**: Crie aplicativos web para estudantes com questões do ENEM.

- **Banco de Questões**: Crie ou Alimente bancos de questões com questões do ENEM.

## 🚀 Rodando

> Para rodar esse projeto você precisa ter o Python (3.6+) e o pip instalados. [Você pode baixar o Python aqui](https://www.python.org/downloads/).

### 1. Instale o Enem Extractor

> Para rodar o **Enem Extractor** via `pip`, execute o seguinte comando no terminal:

```bash
pip install enem
```

### 2. Extraia uma prova

Após a instalação, você pode extrair questões de uma prova em formato PDF. Supondo que você tenha um arquivo de prova do ENEM chamado `prova.pdf` no mesmo diretório, basta rodar:

```bash
python -m enem prova.pdf
```

O script irá analisar a prova e extrair as questões, gerando uma pasta com um arquivo de saída em JSON com os dados extraídos e outros assets da prova. [Veja mais detalhes da saída do comando aqui](#saida).

### 3. Parâmetros adicionais

Você pode fornecer parâmetros adicionais para personalizar o processo de extração:

- `-f` ou `--file`: Caminho para o arquivo PDF da prova. (obrigatório)
- `-g` ou `--key`: Caminho para o arquivo PDF do gabarito. (opcional)
- `-o` ou `--output`: Caminho onde a pasta dos arquivos extraídos será criada. (opcional)

Exemplo de uso com parâmetros:

```bash
python -m enem -f prova.pdf -g gabarito.pdf -o C:\documents
```

Este comando irá extrair as questões da prova `prova.pdf`, corrigir com o gabarito `gabarito.pdf` e salvar a pasta dos resultados em `C:\documents`.

## Saída

 **[Aprenda sobre as saídas que da extração clicando aqui.](examples/output_example/readme.md)**

<img src="https://github.com/user-attachments/assets/9e78b4f0-2055-4f32-a9c5-1bc3e96a2fdc" alt="demo_enem" width="350"/>



## 🔧 Como Contribuir

1. Faça um fork deste repositório.
2. Crie uma venv (`python -m venv venv`) e ative-a (`source venv/bin/activate` ou `venv/script/activate`).
3. Instale as dependências (`pip install -r requirements.txt`).
4. Faça as alterações desejadas, instale o pacote localmente (`pip install -e .`) e teste.
5. Faça o commit das suas alterações (`git commit -am 'Adiciona nova funcionalidade'`).
2. Crie uma branch para a sua modificação (`git checkout -b feature/nova-funcionalidade`).
3. Faça suas alterações e commit (`git commit -am 'Adiciona nova funcionalidade'`).
4. Envie para o repositório original (`git push origin feature/nova-funcionalidade`).
5. Crie um novo Pull Request.

## 📜 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📚 Links Úteis

- [Documentação do PyMuPDF](https://pypi.org/project/PyMuPDF/)
- [Repositório](https://github.com/diaslui/enem-extractor)
- [English version of README](https://github.com/diaslui/enem-extractor/blob/master/README.en.md)

---

### 📢 Issues

Caso você tenha alguma dúvida, queira sugerir melhorias ou encontre problemas, fique à vontade para [abrir um issue](https://github.com/diaslui/enem-extractor/issues).

### 🌀 Subdependências 

- [PyMuPDF](https://pypi.org/project/PyMuPDF/) - PDF parsing 
- [Pillow](https://pypi.org/project/Pillow/) - Image processing 
- [Colorama](https://pypi.org/project/colorama/) - Terminal colors 


Created with ❤️ by [Pedro L. Dias](https://github.com/diaslui)
