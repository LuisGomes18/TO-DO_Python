# -*- coding: utf-8 -*-
import mysql.connector
from json import dump
from extras import carregar_dados_database
from extras import listar_ids
from extras import carregar_conteudo
from extras import mostrar_cartoes
from extras import criar_database
from definicoes import escolha
from definicoes import apagar_terminal


info_database = carregar_dados_database()

try:
    mydb = mysql.connector.connect(
        host=info_database["host"],
        user=info_database["nome_utilizador"],
        password=info_database["password"],
        database=info_database["nome_database"]
    )

    mycursor = mydb.cursor()
except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")
    exit(1)

database_criada = info_database["database_criada"]
if not database_criada:
    criar_database(mydb, mycursor)
    database_criada = True
    try:
        with open('Data/config.json', 'w', encoding='utf-8') as dados:
            dump({"database_criada": database_criada}, dados)
    except FileNotFoundError:
        print('Ficheiro não encontrado')
    except Exception as erro:
        print(f'ERRO: {erro}')

apagar_terminal()

IDs = listar_ids(mycursor)
cartoes = carregar_conteudo(mycursor)

print('\n')

mostrar_cartoes(mycursor)
while True:
    escolha(mydb, mycursor)
