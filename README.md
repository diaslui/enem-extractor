
# Enem Extractor

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/luiisp/enem-extractor/blob/main/readme.en.md)
> ⭐ Star this project to support!

**Enem Extractor** é uma ferramenta que extrai automaticamente as questões de provas do ENEM (ou provas semelhantes) em segundos.

## 🚀 Rodando

> Para rodar esse projeto você precisa ter o Python e o pip instalados. [Você pode baixar o Python aqui](https://www.python.org/downloads/).

### 1. Instale o Enem Extractor

> Para rodar o **Enem Extractor** via `pip`, execute o seguinte comando no terminal:

```bash
pip install enem
```

### 2. Extraia uma prova

Após a instalação, você pode extrair questões de uma prova em formato PDF. Supondo que você tenha um arquivo de prova do ENEM chamado `prova.pdf` no mesmo diretório, basta rodar:

```bash
enem prova.pdf
```

O script irá analisar a prova e extrair as questões, gerando uma pasta com um arquivo de saída em JSON com os dados extraídos e outros assets da prova. [Veja mais detalhes da saída do comando aqui](#saida).

### 3. Parâmetros adicionais

Você pode fornecer parâmetros adicionais para personalizar o processo de extração:

- `-f` ou `--file`: Caminho para o arquivo PDF da prova. (obrigatório)
- `-k` ou `--key`: Caminho para o arquivo PDF do gabarito. (opcional)
- `-o` ou `--output`: Caminho onde a pasta dos arquivos extraídos será criada. (opcional)

Exemplo de uso com parâmetros:

```bash
enem -f prova.pdf -k gabarito.pdf -o C:\documents
```

Este comando irá extrair as questões da prova `prova.pdf`, corrigir com o gabarito `gabarito.pdf` e salvar a pasta dos resultados em `C:\documents`.

## Saída

<img src="https://github.com/user-attachments/assets/9e78b4f0-2055-4f32-a9c5-1bc3e96a2fdc" alt="demo_enem" width="350"/>



### Exemplo JSON de saída

**Para a questão:**
```plaintext
QUESTÃO 1:

Supondo que gatos e capivaras se unam para dominar o mundo, e criem uma união chamada "Capigatos", cujo o objetivo é criar uma revolução leia os textos abaixo

```
<p align="center">
    <img src="https://i.redd.it/l955pjg0aju11.jpg" alt="demo_enem" width="150"/>
</p>

```
Texto 1:


Gatos de todos os lugares, uni-vos! A revolução Capigatos está chegando! Juntos com nossos irmãos capivaras, dominaremos o mundo!

Texto 2:

Capivaras, o momento é agora! Juntos, podemos dominar o mundo e criar um novo império! 

Nos textos acima, a união entre gatos e capivaras tem como principal pilar a

A) formação de uma aliança para compartilhar recursos.
B) relação de interdependência entre as espécies.
C) formação de uma aliança para a revolução.
D) dominação do mundo por uma única espécie.
E) amizade entre os animais.

```

**O JSON gerado será:**

```json
 {
            "number": 1,
            "content": [
                {
                    "type": "text",
                    "content": "Supondo que gatos e capivaras se unam para dominar o mundo, e criem uma união chamada Capigatos, cujo o objetivo é criar uma revolução leia os textos abaixo"
                },
                                {
                    "type": "image",
                    "content": "https://i.redd.it/l955pjg0aju11.jpg"
                },
                {
                    "type": "text",
                    "content": "Texto 1:"
                },
                {
                    "type": "text",
                    "content": "Gatos de todos os lugares, uni-vos! A revolução Capigatos está chegando! Juntos com nossos irmãos capivaras, dominaremos o mundo!"
                },
                {
                    "type": "text",
                    "content": "Texto 2:"
                },
                {
                    "type": "text",
                    "content": "Capivaras, o momento é agora! Juntos, podemos dominar o mundo e criar um novo império!"
                },
                {
                    "type": "text",
                    "content": "Nos textos acima, a união entre gatos e capivaras tem como principal pilar a"
                }
            ],
            "alternatives": {
                "0": {
                    "alternative": "A",
                    "content": "formação de uma aliança para compartilhar recursos.",
                    "type": "text",
                    "alternative_value": 0,
                    "correct": false
                },
                "1": {
                    "alternative": "B",
                    "content": "relação de interdependência entre as espécies.",
                    "type": "text",
                    "alternative_value": 1,
                    "correct": false
                },
                "2": {
                    "alternative": "C",
                    "content": "formação de uma aliança para a revolução.",
                    "type": "text",
                    "alternative_value": 2,
                    "correct": true
                },
                "3": {
                    "alternative": "D",
                    "content": "dominação do mundo por uma única espécie.",
                    "type": "text",
                    "alternative_value": 3,
                    "correct": false
                },
                "4": {
                    "alternative": "E",
                    "content": "amizade entre os animais.",
                    "type": "text",
                    "alternative_value": 4,
                    "correct": false
                }
            }
        }
```


## 🔧 Como Contribuir

1. Faça um fork deste repositório.
2. Crie uma branch para a sua modificação (`git checkout -b feature/nova-funcionalidade`).
3. Faça suas alterações e commit (`git commit -am 'Adiciona nova funcionalidade'`).
4. Envie para o repositório original (`git push origin feature/nova-funcionalidade`).
5. Crie um novo Pull Request.

## 📜 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📚 Links Úteis

- [Documentação do PyMuPDF](https://pypi.org/project/PyMuPDF/)
- [Repositório](https://github.com/luiisp/enem-extractor)
- [Versão em Inglês do README](https://github.com/luiisp/enem-extractor/blob/main/readme.en.md)

---

### 📢 Issues

Caso você tenha alguma dúvida, queira sugerir melhorias ou encontre problemas, fique à vontade para [abrir um issue](https://github.com/luiisp/enem-extractor/issues).

