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
    confrontos_1a_fase = []
    for _ in range(40):
        clube_bloco_I = random.choice(clubes_iniciais['I'])
        clubes_iniciais['I'].remove(clube_bloco_I)

        clube_bloco_II = random.choice(clubes_iniciais['II'])
        clubes_iniciais['II'].remove(clube_bloco_II)

        confronto = {
            'clube_I': clube_bloco_I['clube'],
            'uf_I': clube_bloco_I['uf_origem'],
            'clube_II': clube_bloco_II['clube'],
            'uf_II': clube_bloco_II['uf_origem']
        }
        confrontos_1a_fase.append(confronto)

    return confrontos_1a_fase

def validar_confronto(confronto: Dict[str, str]) -> None:
    """
    Valida um confronto, verificando se possui as chaves esperadas 'clube_I' e 'clube_II'.

    Args:
        confronto: Um dicionário representando um confronto.

    Raises:
        ValueError: Se o confronto não possui as chaves esperadas.
    """
    if not all(chave in confronto for chave in ['clube_I', 'uf_I', 'clube_II', 'uf_II']):
        raise ValueError("O confronto não possui as chaves esperadas 'clube_I', 'uf_I', 'clube_II' e 'uf_II'.")

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
    for idx, confronto in enumerate(confrontos, start=1):
        validar_confronto(confronto)
        clube_I = f"{confronto['clube_I']} ({confronto['uf_I']})"
        clube_II = f"{confronto['clube_II']} ({confronto['uf_II']})"
        print(f"Jogo {idx}: {clube_I} vs {clube_II}")

def renderizar_html(confrontos: List[Dict[str, str]], fase: str) -> str:
    """
    Cria o HTML para os confrontos.

    Args:
        confrontos: Uma lista de dicionários representando os confrontos.
        fase: Uma string representando a fase dos confrontos.

    Returns:
        Uma string contendo o HTML gerado.
    """
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
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
