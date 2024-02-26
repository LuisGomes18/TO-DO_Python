import time

def carregar_ids(mycursor):
    consulta_ids = "SELECT id FROM conteudo"
    mycursor.execute(consulta_ids)
    lista_ids = mycursor.fetchall()

    for IDs in lista_ids:
        print(IDs[0])


def procura_conteudo(mycursor, id):
    busca = f"SELECT * FROM conteudo WHERE id = '{id}'"
    mycursor.execute(busca)

    resultado = mycursor.fetchall()
    if resultado:
        for x in resultado:
            print(x)
    else:
        print("Nenhum conteúdo encontrado com o ID fornecido.")


def mostrar_tudo(mycursor):
    busca = "SELECT * FROM conteudo"
    mycursor.execute(busca)

    resultado = mycursor.fetchall()
    if resultado:
        for x in resultado:
            print(x)
    else:
        print("Nenhum conteúdo encontrado.")


def update_item(mycursor):
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

        mudar = f"UPDATE conteudo SET {campo} = %s WHERE id = %s"
        mycursor.execute(mudar, (valor, id))

        data = "UPDATE conteudo SET data_modificacao = %s WHERE id = %s"
        data_hoje = time.strftime("%Y-%m-%d")
        mycursor.execute(data, (data_hoje, id))

        hora = "UPDATE conteudo SET hora_modificacao = %s WHERE id = %s"
        hora_hoje = time.strftime("%H:%M")
        mycursor.execute(hora, (hora_hoje, id))
        print("Conteúdo atualizado com sucesso!")
    else:
        print("Opção inválida!")

