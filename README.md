# Seminario-C214
![CI-CD]{https://github.com/InajahaCosta/Seminario-C214/actions/workflow/cicd.yml/badge.svg}


Seminário sobre a utilização da ferramenta Pytest.

# Equipe:
- Inajaha Costa Vilas Boas
- Gabriel Silva Zordan

# Pytest 
 Framework de teste em Python que facilita a escrita de testes simples e escaláveis para aplicações. Com pytest, você pode:

- Escrever testes de forma simples e intuitiva.
- Utilizar fixtures para configuração e limpeza de estados antes e depois dos testes.
- Verificar exceções com facilidade.
- Obter relatórios detalhados sobre falhas e erros nos testes.
- Ampliar suas funcionalidades com uma variedade de plugins disponíveis na comunidade.

Fixtures são funções que permitem criar dados de teste ou realizar ações de configuração para seus testes. Elas são úteis para evitar repetição de código e melhorar a organização dos testes. No nosso projeto, utilizamos uma fixture para fornecer diferentes conjuntos de números para testar as operações da calculadora.

# Calculadora

Este é um projeto de uma calculadora simples em Python.

## Funcionalidades

- Adição
- Subtração
- Multiplicação
- Divisão

## Validações

- As entradas devem ser números (inteiros ou decimais).
- A divisão por zero não é permitida.

## Pré-requisitos

- Python 3.6 ou superior
- pytest
- `pip` (gerenciador de pacotes do Python)
- Git (para clonar o repositório)

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/calculator_project.git
cd calculator_project
```
2. Crie um ambiente virtual:
   
```bash
python -m venv venv
source venv/bin/activate # No Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Testes
Para rodar os testes, basta executar o seguinte comando na pasta do projeto: 

Rodar todos os arquivos de teste:

```bash
pytest
```

Rodas um arquivo de teste específico:

```bash
pytest nome_do_arquivo.py
```

## Integração Contínua
Este projeto utiliza GitHub Actions para CI/CD. O workflow está configurado para executar testes, gerar um relatório de testes e empacotar o software. Todos os artefatos são carregados automaticamente.

