from tkinter import *

DEBUG = True


class App:
    def __init__(self, master=None):
        self.tela = Frame(master)
        self.tela.pack()
        self.titulo = Label(self.tela, text='TODO Python')
        self.titulo["font"] = ("Arial", 20, "bold")
        self.titulo.pack()
        self.botao_sair = Button(self.tela, text='Sair', command=self.sair)
        self.botao_sair["font"] = ("Arial", 10, "bold")
        self.botao_sair["fg"] = "black"
        self.botao_sair["bg"] = "white"
        self.botao_sair["width"] = 6
        self.botao_sair.pack()

    def sair(self):
        if not DEBUG:
            self.tela.destroy()
            exit(0)
        else:
            pass


root = Tk()
App(root)
root.mainloop()
