"""
Main script for Trello Python application without a graphical user interface.

This script imports functions from 'extras_sem_gui' and 'def_sem_gui' modules,
loads data, clears the terminal, and enters a loop to make choices.

"""
from extras_sem_gui import carregar_cartoes
from extras_sem_gui import carregar_ids
from extras_sem_gui import apagar_terminal
from def_sem_gui import escolha

apagar_terminal()

dados_IDs = carregar_ids()
IDs = dados_IDs["IDs"]

Cartoes = carregar_cartoes()

while True:
    escolha(IDs, Cartoes, dados_IDs)
