import json
import random
from typing import Dict, List

from jinja2 import Environment, FileSystemLoader

FASE_1 = '1ª'

def load_data() -> Dict[str, List[Dict[str, str]]]:
    """
    Carrega os dados do arquivo JSON.

    Returns:
        Um dicionário contendo os dados carregados.
    """
    with open('copa_do_brasil_2024.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def sortear_confrontos_1a_fase(clubes_iniciais: Dict[str, List[Dict[str, str]]]) -> List[Dict[str, str]]:
    """
    Sorteia os confrontos da 1ª Fase.

    Args:
        clubes_iniciais: Um dicionário contendo os clubes divididos em blocos I e II.

    Returns:
        Uma lista de dicionários representando os confrontos sorteados.
    """
    confrontos_1a_fase = [
        {'clube_I': random.choice(clubes_iniciais['I'])['clube'], 'clube_II': random.choice(clubes_iniciais['II'])['clube']}
        for _ in range(40)
    ]
    return confrontos_1a_fase

def validar_confronto(confronto: Dict[str, str]) -> None:
    """
    Valida um confronto, verificando se possui as chaves esperadas 'clube_I' e 'clube_II'.

    Args:
        confronto: Um dicionário representando um confronto.

    Raises:
        ValueError: Se o confronto não possui as chaves esperadas.
    """
    if not all(chave in confronto for chave in ['clube_I', 'clube_II']):
        raise ValueError("O confronto não possui as chaves esperadas 'clube_I' e 'clube_II'.")

def print_confrontos(confrontos: List[Dict[str, str]], fase: str) -> None:
    """
    Imprime os confrontos.

    Args:
        confrontos: Uma lista de dicionários representando os confrontos.
        fase: Uma string representando a fase dos confrontos.

    Returns:
        None
    """
    print(f"Confrontos da {fase} Fase:")
    for confronto in confrontos:
        validar_confronto(confronto)
        print(f"Jogo {confrontos.index(confronto) + 1}: {confronto['clube_I']} vs {confronto['clube_II']}")

def renderizar_html(confrontos: List[Dict[str, str]], fase: str) -> str:
    """
    cria o HTML para os confrontos.

    Args:
        confrontos: Uma lista de dicionários representando os confrontos.
        fase: Uma string representando a fase dos confrontos.

    Returns:
        None
    """
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('index.html')
    return template.render(confrontos=confrontos, fase=fase)

def main() -> None:
    """
    Função principal que executa o sorteio e imprime os confrontos.
    
    Returns:
        None
    """
    dados_copa_brasil = load_data()

    if 'clubes' not in dados_copa_brasil:
        raise ValueError("Os dados não contêm a chave esperada 'clubes'.")

    clubes_terceira_fase = ['Libertadores', 'Copa do Nordeste', 'Copa Verde', 'Brasileiro Série B', 'Brasileiro Série A']
    clubes_iniciais = [clube for clube in dados_copa_brasil['clubes'] if clube['critério'] not in clubes_terceira_fase]

    blocos = {'I': clubes_iniciais[:40], 'II': clubes_iniciais[40:]}

    confrontos_1a_fase = sortear_confrontos_1a_fase(blocos)
    print_confrontos(confrontos_1a_fase, FASE_1)

    html_content = renderizar_html(confrontos_1a_fase, FASE_1)

    with open('confrontos_1a_fase.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

if __name__ == '__main__':
    main()
