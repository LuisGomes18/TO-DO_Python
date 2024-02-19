# -*- coding: utf-8 -*-
import datetime
from random import randint
from tkinter import *
from tkinter import messagebox

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
            "Data_Criacao": data_hoje.strftime("%d-%m-%Y"),
            "Hora_Criacao": datetime.datetime.now().strftime("%H:%M"),
            "Data_ultima_modificacao": "00-00-0000",
            "Hora_ultima_modificacao": "00:00",
            "ID": id
        }
    }

    dados_IDs['IDs'].append(id)
    guardar_ids(dados_IDs)

    Cartoes.update(cartao)
    guardar_cartoes(Cartoes)


def apagar_todo(self):
    id_ticket = int(self.id_apagar.get())

    if id_ticket not in self.IDs:
        messagebox.showerror("Erro", "ID do Ticket não encontrado.")
        return

    apagar_mesmo = messagebox.askquestion("Apagar Ticket", "Tem certeza que deseja apagar esse Ticket?")
    if apagar_mesmo == "yes":
        Cartoes.pop(str(id_ticket), " ")
        guardar_cartoes(Cartoes)
        self.IDs.remove(str(id_ticket))
        self.dados_IDs['IDs'] = self.IDs
        guardar_ids(self.dados_IDs)
        self.id_apagar.delete(0, 'end')
        messagebox.showinfo("Sucesso", "Ticket apagado com sucesso.")
    else:
        self.id_apagar.delete(0, 'end')
        messagebox.showinfo("Sucesso", "Ticket não apagado.")


class Application:
    def __init__(self, master=None):
        self.master = master
        self.dados_IDs = carregar_ids()
        self.IDs = self.dados_IDs['IDs']
        self.tela()

    def destroy_window(self):
        try:
            self.master.destroy()
        except AttributeError:
            pass

    def tela(self):
        self.destroy_window()
        self.master = Tk()
        self.master.title("TODO Python")
        self.master.geometry("600x600+250+50")

        tela_1 = Frame(self.master)
        tela_1["pady"] = 10
        tela_1.pack()

        tela_2 = Frame(self.master)
        tela_2["pady"] = 10
        tela_2.pack()

        tela_3 = Frame(self.master)
        tela_3.pack()

        tela_4 = Frame(self.master)
        tela_4["pady"] = 100
        tela_4.pack()

        titulo = Label(tela_1, text='TODO Python')
        titulo["font"] = ("Arial", 20, "bold")
        titulo.pack()

        botao_criar = Button(tela_2, text='Criar', command=self.criar)
        botao_criar["font"] = ("Arial", 10, "bold")
        botao_criar["fg"] = "black"
        botao_criar["bg"] = "white"
        botao_criar.pack()

        botao_apagar = Button(tela_3, text='Apagar', command=self.tela_apagar)
        botao_apagar["font"] = ("Arial", 10, "bold")
        botao_apagar["fg"] = "black"
        botao_apagar["bg"] = "white"
        botao_apagar.pack()

        botao_sair = Button(tela_4, text='Sair', command=self.destroy_window)
        botao_sair["font"] = ("Arial", 10, "bold")
        botao_sair["fg"] = "black"
        botao_sair["bg"] = "white"
        botao_sair.pack()

    def criar(self):
        data_hoje = datetime.date.today()

        self.destroy_window()
        self.master = Tk()
        self.master.title("Criar Novo Ticket")
        self.master.geometry("600x600+250+50")

        titulo = Label(self.master, text='Criar Novo Ticket')
        titulo["font"] = ("Arial", 20, "bold")
        titulo.pack()

        tela_1 = Frame(self.master)
        tela_1["pady"] = 10
        tela_1.pack()

        tela_2 = Frame(self.master)
        tela_2["pady"] = 10
        tela_2.pack()

        tela_3 = Frame(self.master)
        tela_3["pady"] = 10
        tela_3.pack()

        tela_4 = Frame(self.master)
        tela_4["pady"] = 10
        tela_4.pack()

        tela_5 = Frame(self.master)
        tela_5["pady"] = 10
        tela_5.pack()

        tela_6 = Frame(self.master)
        tela_6["pady"] = 10
        tela_6.pack()

        titulo_ticket_label = Label(tela_1, text='Título do Ticket')
        titulo_ticket_label["font"] = ("Arial", 10, "bold")
        titulo_ticket_label.pack()

        self.titulo_ticket = Entry(tela_1)
        self.titulo_ticket["font"] = ("Arial", 10, "bold")
        self.titulo_ticket["width"] = 50
        self.titulo_ticket.pack()

        descricao_ticket_label = Label(tela_2, text='Descrição do Ticket')
        descricao_ticket_label["font"] = ("Arial", 10, "bold")
        descricao_ticket_label.pack()

        self.descricao_ticket = Text(tela_2, width=50, height=10)
        self.descricao_ticket["font"] = ("Arial", 10, "bold")
        self.descricao_ticket.pack()

        data_criacao = Label(tela_3, text=f'Data de Criação: {data_hoje.strftime("%d-%m-%Y")}')
        data_criacao["font"] = ("Arial", 10, "bold")
        data_criacao.pack()

        hora_criacao = Label(tela_3, text=f'Hora de Criação: {datetime.datetime.now().strftime("%H:%M")}')
        hora_criacao['font'] = ("Arial", 10, "bold")
        hora_criacao.pack()

        id = self.gerar_novo_id()

        id_label = Label(tela_4, text=f'ID: {id}')
        id_label["font"] = ("Arial", 10, "bold")
        id_label.pack()

        botao_salvar = Button(tela_5, text='Salvar', command=self.salvar_dados)
        botao_salvar["font"] = ("Arial", 10, "bold")
        botao_salvar["fg"] = "black"
        botao_salvar["bg"] = "white"
        botao_salvar["width"] = 6
        botao_salvar.pack()

        botao_voltar = Button(tela_6, text='Voltar', command=self.tela)
        botao_voltar["font"] = ("Arial", 10, "bold")
        botao_voltar["fg"] = "black"
        botao_voltar["bg"] = "white"
        botao_voltar["width"] = 6
        botao_voltar.pack()

    def salvar_dados(self):
        titulo = self.titulo_ticket.get()
        descricao = self.descricao_ticket.get("1.0", "end-1c")
        if len(titulo) == 0 or len(descricao) == 0:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return
        id = self.gerar_novo_id()
        salvar(id, titulo, descricao)
        self.titulo_ticket.delete(0, 'end')
        self.descricao_ticket.delete("1.0", "end")
        self.tela()

    @staticmethod
    def gerar_novo_id():
        id = randint(10000, 99999)
        while id in IDs:
            id = randint(10000, 99999)
        return id

    def tela_apagar(self):
        self.destroy_window()
        self.master = Tk()
        self.master.title("Apagar Ticket")
        self.master.geometry("600x600+250+50")

        self.tela_apagar_1 = Frame(self.master)
        self.tela_apagar_1["pady"] = 10
        self.tela_apagar_1.pack()

        self.tela_apagar_2 = Frame(self.master)
        self.tela_apagar_2["pady"] = 10
        self.tela_apagar_2.pack()

        self.tela_apagar_3 = Frame(self.master)
        self.tela_apagar_3["pady"] = 10
        self.tela_apagar_3.pack()

        self.tela_apagar_4 = Frame(self.master)
        self.tela_apagar_4["pady"] = 10
        self.tela_apagar_4.pack()

        self.tela_apagar_5 = Frame(self.master)
        self.tela_apagar_5.pack()

        self.titulo = Label(self.tela_apagar_1, text='Apagar Ticket')
        self.titulo["font"] = ("Arial", 20, "bold")
        self.titulo.pack()

        self.label_apagar = Label(self.tela_apagar_2, text='ID do Ticket: ')
        self.label_apagar["font"] = ("Arial", 10, "bold")
        self.label_apagar.pack()

        self.id_apagar = Entry(self.tela_apagar_3)
        self.id_apagar["font"] = ("Arial", 10, "bold")
        self.id_apagar["width"] = 50
        self.id_apagar.pack()

        self.botao_apagar = Button(self.tela_apagar_4, text='Apagar', command=lambda: apagar_todo(self))
        self.botao_apagar["font"] = ("Arial", 10, "bold")
        self.botao_apagar["fg"] = "black"
        self.botao_apagar["bg"] = "white"
        self.botao_apagar["width"] = 6
        self.botao_apagar.pack()

        self.botao_voltar = Button(self.tela_apagar_5, text='Voltar', command=self.tela)
        self.botao_voltar["font"] = ("Arial", 10, "bold")
        self.botao_voltar["fg"] = "black"
        self.botao_voltar["bg"] = "white"
        self.botao_voltar["width"] = 6
        self.botao_voltar.pack()


def main():
    root = Tk()
    Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
