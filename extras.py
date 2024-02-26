import mysql.connector
from json import load
from json import JSONDecodeError


def carregar_dados_database():
    try:
        with open('Data/config.json', 'r', encoding='utf-8') as dados:
            informacoes_database = load(dados)
    except JSONDecodeError:
        print('Erro na formatação do JSON')
    except FileNotFoundError:
        print('Ficheiro não encontrado')
    except Exception as erro:
        print(f'ERRO: {erro}')
    else:
        return informacoes_database


def criar_database(mydb, mycursor):
    mycursor.execute("DROP TABLE IF EXISTS conteudo")
    mycursor.execute(
        "CREATE TABLE conteudo (id INT NOT NULL, titulo TINYTEXT NOT NULL, descricao TEXT NOT NULL, tags VARCHAR(255) "
        "NOT NULL, data_criacao DATE NOT NULL, hora_criacao TIME NOT NULL, data_modificacao DATE NOT NULL, "
        "hora_modificacao TIME NOT NULL)")
    mycursor.execute(
        "INSERT INTO conteudo VALUES ('1', 'Teste', 'Teste do TODO', ' ', '2024-02-26', '09:30', '2024-02-26', '09:30')")

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


def carregar_conteudo(mycursor):
    try:
        mostrar_conteudo_todo = "SELECT * FROM conteudo"
        mycursor.execute(mostrar_conteudo_todo)

        cartoes = mycursor.fetchall()
        return cartoes
    except Exception as erro:
        print(f'Erro ao carregar conteúdo: {erro}')


def listar_ids(mycursor):
    try:
        consultar_ids = "SELECT id FROM conteudo"
        mycursor.execute(consultar_ids)
        lista_id = [registro[0] for registro in mycursor.fetchall()]
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ou executar consulta: {e}")
        return []
    else:
        return lista_id


def mostrar_cartoes(mycursor):
    cartoes = carregar_conteudo(mycursor)
    if cartoes:
        print(cartoes)
    else:
        print('Nenhum conteúdo encontrado')
