from tkinter import *


class App:
    def __init__(self, master):
        self.master = master
        self.titulo()
        self.subtitulo()
        self.botao_trocar_tela()

    def titulo(self):
        title = Label(
            self.master, text="TO-DO Python", font=("Helvetica", 14, "bold")
        )
        title.pack()

    def subtitulo(self):
        subtitulo = Label(
            self.master,
            text="Feito em Python 3.12",
            font=("Helvetica", 10, "bold")
        )
        subtitulo.pack()

    def botao_trocar_tela(self):
        button = Button(
            self.master, text="Trocar para Segunda Tela", command=self.trocar_tela)
        button.pack()

    def trocar_tela(self):
        self.master.withdraw()
        self.master.destroy()  # Destroi a primeira tela
        # Cria uma nova instância de Tk para a segunda tela
        segunda_tela = SegundaTela(Tk())
        segunda_tela.mostrar()


class SegundaTela:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
        self.titulo()
        self.botao_voltar()

    def titulo(self):
        title = Label(
            self.frame, text="Segunda Tela", font=("Helvetica", 14, "bold")
        )
        title.pack()

    def botao_voltar(self):
        button = Button(
            self.frame, text="Voltar para Tela Inicial", command=self.voltar_tela)
        button.pack()

    def voltar_tela(self):
        self.master.withdraw()
        self.master.destroy()  # Destroi a segunda tela
        root = Tk()  # Cria uma nova instância de Tk para a tela inicial
        app = App(root)
        root.mainloop()

    def mostrar(self):
        self.master.deiconify()


root = Tk()
app = App(root)
root.mainloop()
