import datetime
from random import randint
from tkinter import *
from extras_sem_gui import guardar_ids, carregar_ids, apagar_terminal, carregar_cartoes, guardar_cartoes

apagar_terminal()
dados_IDs = carregar_ids()
IDs = dados_IDs['IDs']
Cartoes = carregar_cartoes()


def salvar(id, titulo, descricao):
    data_hoje = datetime.date.today()

    cartao = {
        f"{id}": {
            "Titulo": titulo,
            "Descricao": descricao,
            "Tag": [],
            "Data de Criacao": data_hoje.strftime("%d-%m-%Y"),
            "Hora de Criacao": datetime.datetime.now().strftime("%H:%M"),
            "Data_ultima_modificacao": "00-00-0000",
            "Hora_ultima_modificacao": "00:00",
            "ID": id
        }
    }

    dados_IDs['IDs'].append(cartao[f"{id}"]["ID"])
    guardar_ids(dados_IDs)

    Cartoes.update(cartao)
    guardar_cartoes(Cartoes)


class Application:
    def __init__(self, master=None):
        self.master = master
        self.criar_interface()

    def criar_interface(self):
        data_hoje = datetime.date.today()

        self.tela_1 = Frame(self.master)
        self.tela_1["pady"] = 10
        self.tela_1.pack()

        self.tela_2 = Frame(self.master)
        self.tela_2["pady"] = 10
        self.tela_2.pack()

        self.tela_3 = Frame(self.master)
        self.tela_3["pady"] = 10
        self.tela_3.pack()

        self.tela_4 = Frame(self.master)
        self.tela_4["pady"] = 10
        self.tela_4.pack()

        self.tela_5 = Frame(self.master)
        self.tela_5["pady"] = 10
        self.tela_5.pack()

        self.tela_6 = Frame(self.master)
        self.tela_6["pady"] = 10
        self.tela_6.pack()

        self.tela_7 = Frame(self.master)
        self.tela_7["pady"] = 10
        self.tela_7.pack()

        self.titulo = Label(self.tela_1, text='TODO Python')
        self.titulo["font"] = ("Arial", 20, "bold")
        self.titulo.pack()

        self.titulo_ticket_label = Label(self.tela_2, text='Título do Título')
        self.titulo_ticket_label["font"] = ("Arial", 10, "bold")
        self.titulo_ticket_label.pack()

        self.titulo_ticket = Entry(self.tela_2)
        self.titulo_ticket["font"] = ("Arial", 10, "bold")
        self.titulo_ticket["width"] = 50
        self.titulo_ticket.pack()

        self.descricao_ticket_label = Label(self.tela_3, text='Descrição do Ticket')
        self.descricao_ticket_label["font"] = ("Arial", 10, "bold")
        self.descricao_ticket_label.pack()

        self.descricao_ticket = Text(self.tela_3, width=50, height=10)
        self.descricao_ticket["font"] = ("Arial", 10, "bold")
        self.descricao_ticket.pack()

        self.data_criacao = Label(self.tela_4, text=f'Data de Criação: {data_hoje.strftime("%d-%m-%Y")}')
        self.data_criacao["font"] = ("Arial", 10, "bold")
        self.data_criacao.pack()

        self.hora_criacao = Label(self.tela_4, text=f'Hora de Criação: {datetime.datetime.now().strftime("%H:%M")}')
        self.hora_criacao['font'] = ("Arial", 10, "bold")
        self.hora_criacao.pack()

        id = randint(10000, 99999)
        while id in IDs:
            id = randint(10000, 99999)

        self.id_label = Label(self.tela_5, text=f'ID: {id}')
        self.id_label["font"] = ("Arial", 10, "bold")
        self.id_label.pack()

        self.botao_salvar = Button(self.tela_6, text='Salvar', command=self.salvar_dados)
        self.botao_salvar["font"] = ("Arial", 10, "bold")
        self.botao_salvar["fg"] = "black"
        self.botao_salvar["bg"] = "white"
        self.botao_salvar["width"] = 6
        self.botao_salvar.pack()

    def salvar_dados(self):
        titulo = self.titulo_ticket.get()
        descricao = self.descricao_ticket.get("1.0", "end-1c")
        id = self.gerar_novo_id()
        salvar(id, titulo, descricao)
        self.atualizar_id()
        # Limpar campos de entrada
        self.titulo_ticket.delete(0, 'end')
        self.descricao_ticket.delete("1.0", "end")

    def gerar_novo_id(self):
        id = randint(10000, 99999)
        while id in IDs:
            id = randint(10000, 99999)
        return id

    def atualizar_id(self):
        id = randint(10000, 99999)
        while id in IDs:
            id = randint(10000, 99999)

        self.id_label.config(text=f'ID: {id}')


root = Tk()
Application(root)
root.mainloop()
