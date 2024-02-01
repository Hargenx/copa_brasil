# Copa do Brasil 2024 - Sorteio de Confrontos

Este é um programa Python para simular o sorteio de confrontos da Copa do Brasil 2024. O programa utiliza dados fornecidos em um arquivo JSON que contém informações sobre os clubes participantes e os critérios para entrada na competição.

Dados usados e alguns crietérios:

https://www.cbf.com.br/futebol-brasileiro/noticias/copa-brasil/copa-do-brasil-2024-confira-os-documentos-tecnicos

Obviamente é só uma brincadeira feita em 40 minutos durante o segundo tempo de Flamengo e Sampaio Coreia pela quarta rodada do Estadua do Rio de Janeiro, logo, lol....

![A taça](image.png)


## Pré-requisitos

- Python 3.x
- Biblioteca `jinja2` (instalável com `pip install Jinja2`)

## Uso

1. Clone este repositório:

   ```bash
   git clone https://github.com/Hargenx/copa-do-brasil-2024.git
   cd copa-do-brasil-2024
    ```

2. Execute o programa:
    ```bash
    python main.py
    ```
    Este comando gerará um arquivo HTML chamado confrontos_1a_fase.html com os confrontos da 1ª fase.


3. Abra o arquivo HTML gerado em um navegador para visualizar os confrontos.

## Estrutura do Projeto

copa_do_brasil_2024.json: Arquivo JSON contendo informações sobre os clubes e critérios.
sorteio_confrontos.py: Código-fonte principal para sorteio de confrontos.
index.html: Template HTML para exibição dos confrontos.

## Contribuições

Contribuições são bem-vindas! Se encontrar algum problema ou tiver sugestões de melhorias, por favor, abra uma issue.

## Licença

Este projeto é distribuído sob a [Licença MIT](LICENSE).
