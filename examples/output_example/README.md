# Saída da extração

**O que esse exemplo considera?**

Esse exemplo considera que você já tenha extraído os dados de uma prova do Enem com o Enem Extractor usando o comando `enem prova.pdf gabarito.pdf`. Se você ainda não fez isso, [clique aqui para ver como isso pode ser feito](https://github.com/luiisp/enem-extractor?tab=readme-ov-file#saida).

----------------

### Primeiras Impressões

O Enem Extractor sempre irá gerar uma pasta chamada `output_[nome do seu pdf]` com os arquivos extraídos. (Nesse exemplo o nome da pasta é `output_prova` pois o arquivo da prova que foi extraído tem nome de `prova.pdf`)

### Estrutura Base

```
|__ output_prova
|   |
|   |___img__ [imagens extraídas]
|   |
|   |__ output.json
```

A pasta gerada com nome `img` contém todas as imagens extraídas da prova.

----------------

#### Sobre as imagens

As imagens extraídas são as imagens das questões da prova. Elas são referenciadas no arquivo `output.json` (veremos isso mais à frente), elas sempre estarão em formato `.png`.

----------------

O arquivo `output.json` contém todos os dados extraídos da prova.

## Output.json

O arquivo `output.json` é um arquivo JSON que contém todos os dados extraídos da prova. Ele é o arquivo principal que você irá usar para manipular os dados extraídos.

### Entendendo a estrutura do arquivo

Todos os dados relevantes sobre a prova estão contidos dentro do objeto principal do JSON que é um array de objetos chamado `data`.

**Então por enquanto, a estrutura do arquivo é a seguinte:**

```json
{
    "data": [
    ]
}
```

Dentro de `data`, que é um array, teremos finalmente **as questões!**.

Como `data` é um array, cada questão será um objeto dentro desse array, espalhados em ordem de aparição na prova (crescente).

#### Por dentro do objeto de uma questão

O objeto de uma questão terá respectivamente os seguintes campos:

- `number` **number** : Número real da questão
- `content` **array** : Conteúdo da questão (Enunciado)
- `alternatives` **object** : Array de objetos com as alternativas da questão

**Content** é um array de objetos que estará em ordem crescente conforme aparecem na questão.

Dentro de `content` teremos os seguintes campos:

- `type` **string** : Tipo do conteúdo (text, image)
- `content` **string** : Valor do conteúdo

Se `type` for `image`, `content` será o caminho da imagem extraída.

Se `type` for `text`, `content` será o texto extraído.

**Alternatives** é um objeto que contém as alternativas da questão.

Dentro de `alternatives` teremos os objetos das alternativas da questão em ordem, cada objeto terá os seguintes campos:

- `alternative` **string** : Letra da alternativa (A, B, C, D, E)
- `content` **string** : Conteúdo da alternativa
- `type` **string** : Tipo do conteúdo (text, image)
- `alternative_value` **string** : Valor da alternativa em número (0, 1, 2, 3, 4)
- `correct` **boolean** : Se a alternativa é correta ou não

O conteúdo de uma alternativa pode ser uma imagem ou texto, se for uma imagem, `content` será o caminho da imagem extraída.

***A estrutura final da questão fica:***

```json
{
    "number": 1,
    "content": [
        {
            "type": "text",
            "content": "Enunciado da questão"
        },
        {
            "type": "image",
            "content": "img/1.png"
        }
    ],
    "alternatives": {
        "A": {
            "alternative": "A",
            "content": "Conteúdo da alternativa A",
            "type": "text",
            "alternative_value": "0",
            "correct": false
        },
        "B": {
            "alternative": "B",
            "content": "Conteúdo da alternativa B",
            "type": "text",
            "alternative_value": "1",
            "correct": true
        },
        "C": {
            "alternative": "C",
            "content": "Conteúdo da alternativa C",
            "type": "text",
            "alternative_value": "2",
            "correct": false
        },
        "D": {
            "alternative": "D",
            "content": "Conteúdo da alternativa D",
            "type": "text",
            "alternative_value": "3",
            "correct": false
        },
        "E": {
            "alternative": "E",
            "content": "Conteúdo da alternativa E",
            "type": "text",
            "alternative_value": "4",
            "correct": false
        }
    }
}
```


---

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

----------------

### Conclusão

Esse é o básico sobre a saída da extração. Com essas informações você já pode manipular os dados extraídos da prova do Enem à vontade.

### Próximos passos

Agora que você já sabe como é a saída da extração, você pode começar a manipular os dados extraídos. [Clique aqui para ver um exemplo de como isso pode ser feito](https://github.com/luiisp/enem-extractor/tree/master/examples/data_usage).
