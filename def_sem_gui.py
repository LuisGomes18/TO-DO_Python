# pylint: disable=invalid-name
"""
Trello Python Module

This module provides functions for managing Trello-like cards. It includes functions
to create, modify, and delete cards, as well as utility functions for handling IDs
and storing card data.

Classes:
- SetEncoder: Custom JSONEncoder for handling sets.

Functions:
- escolha: Function to choose between creating, modifying, deleting cards, or exiting.
- criar_cartao: Function to create a new card.
- modificar_cartao: Function to modify an existing card.
- apagar_cartao: Function to delete an existing card.
"""
import datetime
from json import JSONEncoder
from random import randint
from extras_sem_gui import guardar_ids
from extras_sem_gui import guardar_cartoes
from extras_sem_gui import mostrar_cartoes


class SetEncoder(JSONEncoder):
    """
        Custom JSON encoder for handling sets.

        Parameters:
        - obj: The object to encode.

        Returns:
        - JSON-encoded object.
    """

    def default(self, obj):
        """
        Custom JSON encoder for handling sets.

        Parameters:
        - obj: The object to encode.

        Returns:
        - JSON-encoded object.
        """
        if isinstance(obj, set):
            return list(obj)
        return JSONEncoder.default(self, obj)


def escolha(IDs, Cartoes, dados_IDs):
    """
    Função para escolher entre criar, modificar, apagar cartão ou sair.

    Parameters:
    - IDs: Lista de IDs existentes.
    - Cartoes: Dicionário contendo os cartões.
    - dados_IDs: Dicionário contendo os dados relacionados aos IDs.

    Returns:
    - None
    """
    esc = int(
        input('1) Criar Cartão\n2) Modificar cartao existente\n3) Apagar cartão\n0) Sair \n  -> '))
    if esc == 1:
        criar_cartao(Cartoes, IDs, dados_IDs)
    elif esc == 2:
        modificar_cartao(IDs, Cartoes)
    elif esc == 3:
        apagar_cartao(IDs, Cartoes, dados_IDs)
    elif esc == 0:
        print('\n')
        exit(0)
    else:
        print('\nValor Invalido\n')
        exit(1)


def criar_cartao(Cartoes, IDs, dados_IDs):
    """
    Função para criar um novo cartão.

    Parameters:
    - Cartoes: Dicionário contendo os cartões.
    - IDs: Lista de IDs existentes.
    - dados_IDs: Dicionário contendo os dados relacionados aos IDs.

    Returns:
    - None
    """
    data_hoje = datetime.date.today()
    data = data_hoje.strftime("%d-%m-%Y")
    hora = datetime.datetime.now().strftime("%H:%M")

    titulo = str(input('\nQual nome do cartão: '))
    descricao = str(input('Qual será a descrição do cartão: '))
    ID = randint(10000, 99999)

    while ID in IDs:
        ID = randint(10000, 99999)

    cartao = {
        f"{ID}": {
            "Titulo": titulo,
            "Descricao": descricao,
            "Tag": [],
            "Data_de_criacao": data,
            "Hora_de_criacao": hora,
            "Data_ultima_modificacao": "00-00-0000",
            "Hora_ultima_modificacao": "00:00",
            "ID": ID
        }
    }

    dados_IDs['IDs'].append(ID)
    guardar_ids(dados_IDs)

    Cartoes.update(cartao)
    guardar_cartoes(Cartoes)

    print(f"\nSeu cartão foi guardado com o id {ID}\n")


def modificar_cartao(IDs, Cartoes):
    """
    Função para modificar um cartão existente.

    Parameters:
    - IDs: Lista de IDs existentes.
    - Cartoes: Dicionário contendo os cartões.

    Returns:
    - None
    """
    elemento_permitido = ['titulo', 'descricao', 'tag']
    mostrar_cartoes(Cartoes)

    pedir_id = int(input('Qual ID do cartão que quer modificar: '))
    while pedir_id not in IDs or len(str(pedir_id)) > 5 or len(str(pedir_id)) < 5:
        print('\nID inválido. Coloque um ID válido.')
        pedir_id = int(input('Qual ID do cartão que quer modificar: '))

    elemento = str(input('Qual elemento quer modificar: (titulo, descricao, tag)\n-> '))
    elemento.lower()
    while elemento not in elemento_permitido:
        elemento = str(input('Qual elemento quer modificar: (titulo, descricao, tag)\n-> '))
        elemento.lower()

    if elemento == "titulo":
        data_atual = datetime.date.today().strftime("%d-%m-%Y")
        hora_atual = datetime.datetime.now().strftime("%H:%M")
        novo_titulo = str(input('Qual é o novo nome do cartão: '))
        Cartoes[f"{pedir_id}"]['Titulo'] = novo_titulo
        Cartoes[f"{pedir_id}"]['Data_ultima_modificacao'] = data_atual
        Cartoes[f"{pedir_id}"]['Hora_ultima_modificacao'] = hora_atual
        guardar_cartoes(Cartoes)

    elif elemento == "descricao":
        data_atual = datetime.date.today().strftime("%d-%m-%Y")
        hora_atual = datetime.datetime.now().strftime("%H:%M")
        nova_descricao = str(input('Qual é a nova descrição do cartão: '))
        Cartoes[f"{pedir_id}"]['Descricao'] = nova_descricao
        Cartoes[f"{pedir_id}"]['Data_ultima_modificacao'] = data_atual
        Cartoes[f"{pedir_id}"]['Hora_ultima_modificacao'] = hora_atual
        guardar_cartoes(Cartoes)

    elif elemento == "tag":
        data_atual = datetime.date.today().strftime("%d-%m-%Y")
        hora_atual = datetime.datetime.now().strftime("%H:%M")
        numero_tag = int(input('Quantas tags quer adicionar ao cartão: '))
        tags = []

        for i in range(numero_tag):
            nova_tag = input('Qual é a nova tag do cartão: ')
            nova_tag_mod = nova_tag.replace(" ", "_").replace("@", "")
            nova_tag_mod = "@" + nova_tag_mod
            verificacao = int(input(f'Sua tag {nova_tag_mod} está correta? (1- Sim e 2- Não)\n-> '))
            if verificacao == 1:
                tags.append(nova_tag_mod)
            elif verificacao == 2:
                pass
            else:
                print('Valor Inválido')
                exit(1)

        Cartoes[f"{pedir_id}"]['Tag'].append(nova_tag_mod)
        Cartoes[f"{pedir_id}"]['Data_ultima_modificacao'] = data_atual
        Cartoes[f"{pedir_id}"]['Hora_ultima_modificacao'] = hora_atual
        guardar_cartoes(Cartoes)

    else:
        print('Valor Invalido')
        exit(1)


def apagar_cartao(IDs, Cartoes, dados_IDs):
    """
    Função para apagar um cartão existente.

    Parameters:
    - IDs: Lista de IDs existentes.
    - Cartoes: Dicionário contendo os cartões.
    - dados_IDs: Dicionário contendo os dados relacionados aos IDs.

    Returns:
    - None
    """
    mostrar_cartoes(Cartoes)
    id = int(input('\nQual ID do cartão que quer apagar: '))
    while id not in IDs:
        print('\nID inválido. Coloque um ID válido.')
        id = int(input('Qual ID do cartão que quer apagar: '))
    Cartoes.pop(f"{id}")
    guardar_cartoes(Cartoes)
    IDs.remove(id)
    dados_IDs['IDs'] = IDs
    guardar_ids(dados_IDs)
