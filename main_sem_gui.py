# -*- coding: utf-8 -*-
import mysql.connector
from extras import carregar_dados_database
from extras import listar_ids
from extras import carregar_conteudo
from extras import mostrar_cartoes
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


apagar_terminal()

IDs = listar_ids(mycursor)
cartoes = carregar_conteudo(mycursor)

print('\n')

mostrar_cartoes(mycursor)
while True:
    escolha(mydb, mycursor)
