# 💧 Classificador de Consumo de Água

Uma aplicação em **Python** que classifica o perfil de consumo de água de um imóvel e exibe mensagens educativas de acordo com o tipo de imóvel e o consumo mensal.

## 🎯 Objetivo

Este projeto foi desenvolvido como atividade prática do curso de **Desenvolvimento de Sistemas**, simulando uma campanha de conscientização ambiental de uma companhia de saneamento.

O programa permite:

* 🏠 Identificar o tipo de imóvel.
* 🚰 Informar o consumo mensal de água em m³.
* 📊 Classificar o perfil de consumo.
* 💡 Exibir um alerta ou orientação conforme as regras do exercício.

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github\&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge\&logo=visual-studio-code\&logoColor=white)

## 📐 Regras de classificação

O programa utiliza estruturas condicionais (`if`, `elif` e `else`) para determinar a mensagem exibida ao usuário.

| 🏠 Situação                                   | 💧 Resultado              |
| --------------------------------------------- | ------------------------- |
| Imóvel **comercial**                          | Tarifa comercial aplicada |
| Apartamento com consumo **menor que 10 m³**   | Consumo econômico         |
| Apartamento com consumo **a partir de 10 m³** | Consumo moderado          |
| Casa com consumo de **até 25 m³**             | Consumo moderado          |
| Casa acima de **25 m³**                       | Consumo excessivo         |

### ✅ Validação

Antes da classificação, o programa verifica se o tipo de imóvel informado é válido.

Tipos aceitos:

* `comercial`
* `casa`
* `apartamento`

Caso o usuário digite outro valor, o programa exibe uma mensagem de erro e encerra a execução.

## ▶️ Como executar

1. Clone este repositório:

```bash
git clone https://github.com/gustavoacrani/consumo-agua.git
```

2. Entre na pasta do projeto:

```bash
cd consumo-agua
```

3. Execute o programa:

```bash
python app.py
```

## 💻 Exemplo de uso

```text
Tipo de imóvel (comercial, casa ou apartamento): apartamento
Consumo mensal de água (m³): 8

Consumo econômico – excelente controle de água!
```

### Outro exemplo

```text
Tipo de imóvel (comercial, casa ou apartamento): casa
Consumo mensal de água (m³): 32

Consumo excessivo – adote medidas de economia e verifique vazamentos.
```

### Exemplo de entrada inválida

```text
Tipo de imóvel (comercial, casa ou apartamento): fazenda

Tipo de imóvel inválido. Por favor, insira 'comercial', 'casa' ou 'apartamento'.
```

## 📚 Conceitos praticados

Durante o desenvolvimento deste exercício foram utilizados:

* Entrada de dados com `input()`
* Conversão de tipos (`float()`)
* Operadores lógicos (`and`, `or` e `not in`)
* Estruturas condicionais (`if`, `elif` e `else`)
* Validação de entrada do usuário

## 👨‍💻 Autor

Desenvolvido por **Gustavo Tisiani Acrani** como atividade prática do curso de **Desenvolvimento de Sistemas**.
