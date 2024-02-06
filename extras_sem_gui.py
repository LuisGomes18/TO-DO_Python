# pylint: disable=invalid-name
# pylint: disable=W0718
"""
Script to handle loading, saving, and managing card data.

This script includes functions for loading and saving card information from/to JSON files,
as well as functions for clearing the terminal and displaying card details.
"""
from json import load
from json import dump
from json import JSONDecodeError
import platform
from os import system
from os import path
from os import getcwd


def carregar_cartoes():
    """
    Carrega os dados dos cartões a partir do arquivo JSON.

    Returns:
    - cartoes (dict): Dicionário contendo os dados dos cartões.
    """
    try:
        with open('Data/cartoes.json', 'r', encoding='utf-8') as info_cartoes:
            cartoes = load(info_cartoes)
    except JSONDecodeError:
        print('Erro na formatação do JSON')
    except FileNotFoundError:
        print('Ficheiro não encontrado')
    except Exception as erro:
        print(f'ERRO: {erro}')
    else:
        return cartoes


def guardar_cartoes(cartao):
    """
    Guarda os dados do cartão no arquivo JSON.

    Args:
    - cartao (dict): Dados do cartão a serem salvos.
    """
    file_path = path.join(getcwd(), 'Data', 'cartoes.json')
    try:
        with open(file_path, "w", encoding="utf-8") as info_cartoes:
            dump(cartao, info_cartoes, indent=4)
    except JSONDecodeError:
        print('Erro na formatação do JSON')
    except FileNotFoundError:
        print('Ficheiro não encontrado')
    except Exception as erro:
        print(f'ERRO: {erro}')


def carregar_ids():
    """
    Carrega os IDs a partir do arquivo JSON.

    Returns:
    - IDs (dict): Dicionário contendo os IDs.
    """
    try:
        with open('Data/ids.json', 'r', encoding='utf-8') as dados:
            IDs = load(dados)
    except JSONDecodeError:
        print('Erro na formatação do JSON')
    except FileNotFoundError:
        print('Ficheiro não encontrado')
    except Exception as erro:
        print(f'ERRO: {erro}')
    else:
        return IDs


def guardar_ids(ids):
    """
    Guarda os IDs no arquivo JSON.

    Args:
    - ids (dict): Dados dos IDs a serem salvos.
    """
    file_path = path.join(getcwd(), 'Data', 'ids.json')
    try:
        with open(file_path, 'w', encoding='utf-8') as dados:
            dump(ids, dados, indent=4)
    except JSONDecodeError:
        print('Erro na formatação do JSON')
    except FileNotFoundError:
        print('Ficheiro não encontrado')
    except Exception as erro:
        print(f'ERRO: {erro}')


def apagar_terminal():
    """
    Limpa o terminal com base no sistema operacional.
    """
    os_name = platform.system()
    try:
        if os_name == "Linux" or os_name == "Darwin":
            system("clear")
        elif os_name == "Windows":
            system("cls")
        else:
            print("Sistema não reconhecido")
    except Exception as e:
        print(f'Erro ao tentar limpar o terminal: {e}')
        exit(1)


def mostrar_cartoes(Cartoes):
    """
    Mostra os detalhes dos cartões.

    Args:
    - Cartoes (dict): Dicionário contendo os dados dos cartões.
    """
    print('Cartões todos: \n')
    for chave, cartao in Cartoes.items():
        for campo, conteudo in cartao.items():
            if isinstance(conteudo, list):
                tags = ', '.join(conteudo)
                print(f'{campo}: {tags}')
            else:
                print(f'{campo}: {conteudo}')
        print('\n')
