from time import strftime
from random import randint
from extras import listar_ids
from os import system
import platform


def apagar_terminal():
    try:
        os_name = str(platform.system())
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
    except Exception as os_error:
        print(f'Erro ao identificar o Sistema\nError: {os_error}')
        exit(1)


def escolha(mydb, mycursor):
    escolha = int(input('''
1) Criar Cartão
2) Modificar cartao existente
3) Apagar Cartão
0) Sair 
-> '''))
    match escolha:
        case 1:
            criar_cartao(mydb, mycursor)
        case 2:
            modificar_cartao(mydb, mycursor)
        case 3:
            apagar_cartao(mydb, mycursor)
        case 0:
            exit(0)
        case _:
            print('Valor Invalido')
            pass


def criar_cartao(mydb, mycursor):
    print('\n')
    lista_id = listar_ids(mycursor)

    data_criacao = strftime("%Y-%m-%d")
    hora_criacao = strftime("%H:%M")
    data_modificacao = strftime("%Y-%m-%d")
    hora_modificacao = strftime("%H:%M")
    criar_todo = ("INSERT INTO conteudo (id, titulo, descricao, tags, data_criacao, hora_criacao, data_modificacao, "
                  "hora_modificacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

    ID = randint(10000, 99999)
    while ID in lista_id:
        ID = randint(10000, 99999)

    titulo = input('Qual será o nome do cartão: ')
    descricao = input('Qual será a descrição do cartão: ')
    tags = input('Insira as tags (vazio para nenhuma): ')

    mycursor.execute(criar_todo,
                     (ID, titulo, descricao, tags, data_criacao, hora_criacao, data_modificacao, hora_modificacao))

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")
    print("Conteúdo criado com sucesso!")


def modificar_cartao(mydb, mycursor):
    print('\n')
    lista_id = listar_ids(mycursor)

    id = int(input('Qual o id do conteúdo que quer mudar: '))
    while id not in lista_id:
        id = int(input('Qual o id do conteúdo que quer mudar: '))

    nome_conteudo_mudar = int(input('''
1) Título
2) Descrição
3) Tags  
-> '''))

    if nome_conteudo_mudar in [1, 2, 3]:
        valor = input('Insira o novo valor: ')
        if nome_conteudo_mudar == 1:
            campo = "titulo"
        elif nome_conteudo_mudar == 2:
            campo = "descricao"
        else:
            campo = "tags"

        mudar = f"UPDATE conteudo SET {campo} = %s, data_modificacao = %s, hora_modificacao = %s WHERE id = %s"
        data_hoje = strftime("%Y-%m-%d")
        hora_hoje = strftime("%H:%M")
        values = (valor, data_hoje, hora_hoje, id)

        mycursor.execute(mudar, values)

        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        print("Conteúdo atualizado com sucesso!")
    else:
        print("Opção inválida!")


def apagar_cartao(mydb, mycursor):
    print('\n')
    lista_ids = listar_ids(mycursor)
    tentativas = 0
    while tentativas < 3:
        id = int(input('Qual o id do conteúdo que quer deletar: '))
        if id in lista_ids:
            apagar = "DELETE FROM conteudo WHERE id = %s"
            mycursor.execute(apagar, (id,))
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
            print("Conteúdo deletado com sucesso!")
            return
        else:
            tentativas += 1
            print("ID inválido. Tente novamente.")
    print("Número máximo de tentativas excedido. Operação cancelada.")
