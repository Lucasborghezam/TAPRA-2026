# TAPRA-2026

Projeto da disciplina de Tópicos Avançados em Programação, desenvolvido com Azure Functions.

## Integrantes

- Caio Izabel Grubba
- Lucas Alexandre Borghezam
- Gabriel Tomaz Rodrigues

## Descrição

O projeto contém três Azure Functions:

- **TAPRA2026** (Timer Trigger): executa a cada minuto (`0 * * * * *`) e apenas imprime um log no terminal.
- **receber** (HTTP Trigger): rota `GET /api/receber`, recebe o parâmetro `parametro` via URL e retorna esse valor na resposta.
- **timer_http** (Timer Trigger): executa a cada minuto e faz uma chamada HTTP para a function `receber`, imprimindo no log a resposta recebida.

## Tecnologias

- Azure Functions
- Python
- Biblioteca `requests` (usada na chamada HTTP entre functions)

## Como executar

1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Configure o Azure Functions Core Tools localmente
4. Execute com `func start`

> **Atenção:** o `requirements.txt` atual não lista a biblioteca `requests`, usada em `timer_http`. Adicione `requests` ao arquivo antes de rodar/publicar, senão a function vai falhar.
