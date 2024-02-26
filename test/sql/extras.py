import time
from random import randint
import mysql.connector


def carregar_ids(mycursor):
    try:
        consulta_ids = "SELECT id FROM conteudo"
        mycursor.execute(consulta_ids)
        lista_ids = [registro[0] for registro in mycursor.fetchall()]

    except mysql.connector.Error as e:
        print(f"Erro ao conectar ou executar consulta: {e}")
        return []

    return lista_ids


def procura_conteudo(mycursor, id):
    busca = "SELECT * FROM conteudo WHERE id = %s"
    mycursor.execute(busca, (id,))

    resultado = mycursor.fetchall()
    if resultado:
        for conteudo in resultado:
            print(conteudo)
    else:
        print("Nenhum conteúdo encontrado com o ID fornecido.")


def mostrar_tudo(mycursor):
    busca = "SELECT * FROM conteudo"
    mycursor.execute(busca)

    resultado = mycursor.fetchall()
    if resultado:
        for conteudo in resultado:
            print(conteudo)
    else:
        print("Nenhum conteúdo encontrado.")


def update_item(mydb, mycursor):
    id = int(input('Qual o id do conteudo que quer mudar: '))

    nome_conteudo_mudar = input('''
1) Título
2) Descrição
3) Tags  
->''')

    if nome_conteudo_mudar in ['1', '2', '3']:
        valor = input('Insira o novo valor: ')
        if nome_conteudo_mudar == '1':
            campo = "titulo"
        elif nome_conteudo_mudar == '2':
            campo = "descricao"
        else:
            campo = "tags"

        mudar = f"UPDATE conteudo SET {campo} = %s, data_modificacao = %s, hora_modificacao = %s WHERE id = %s"
        data_hoje = time.strftime("%Y-%m-%d")
        hora_hoje = time.strftime("%H:%M")
        mycursor.execute(mudar, (valor, data_hoje, hora_hoje, id))

        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")

        print("Conteúdo atualizado com sucesso!")
    else:
        print("Opção inválida!")


def criar(mydb, mycursor):
    criar_todo = ("INSERT INTO conteudo (id, titulo, descricao, tags, data_criacao, hora_criacao, data_modificacao, "
                  "hora_modificacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    lista_ids = carregar_ids(mycursor)
    id = randint(10000, 99999)
    while id in lista_ids:
        id = randint(10000, 99999)
    titulo = input('Insira o nome do titulo: ')
    descricao = input('Insira a descrição: ')
    tags = input('Insira as tags (vazio para nenhuma): ')
    data_criacao = time.strftime("%Y-%m-%d")
    hora_criacao = time.strftime("%H:%M")
    data_modificacao = time.strftime("%Y-%m-%d")
    hora_modificacao = time.strftime("%H:%M")
    mycursor.execute(criar_todo,
                     (id, titulo, descricao, tags, data_criacao, hora_criacao, data_modificacao, hora_modificacao))
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

    print("Conteúdo criado com sucesso!")


def deletar(mydb, mycursor):
    lista_ids = carregar_ids(mycursor)
    tentativas = 0
    while tentativas < 3:
        id = int(input('Qual o id do conteudo que quer deletar: '))
        if id in lista_ids:
            apagar = "DELETE FROM conteudo WHERE id = %s"
            mycursor.execute(apagar, (id,))
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
            print("Conteúdo deletado com sucesso!")
            return
        else:
            tentativas += 1
            print("Id inválido. Tente novamente.")

    print("Número máximo de tentativas excedido. Operação cancelada.")
