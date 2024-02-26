import mysql.connector
from extras import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Luisg@mes19!",
    database="to-do_python_teste"
)

mycursor = mydb.cursor()
carregar_ids(mycursor)

while True:
    escolha = int(input("""
1) Ver conteudo (id)
2) Mostrar tabela inteira
3) Mudar valor
0) Sair
-> """))
    match escolha:
        case 1:
            id = input('Insira o id do conteudo: ')
            procura_conteudo(mycursor, id)
        case 2:
            mostrar_tudo(mycursor)
        case 3:
            update_item(mycursor)
        case 0:
            break
        case _:
            print('Valor Invalido')

mydb.close()
