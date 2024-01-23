from tkinter import *  # ANCHOR - Lista de modulos


# SECTION - Aolicação
class App:
    def __init__(self, master):
        self.master = master
        self.titulo()
        self.subtitulo()

    #ANCHOR -  Definição do titulo
    def titulo(self):
        title = Label(
            self.master, text="TO-DO Python", font=("Helvetica", 14, "bold")
        )  # TODO Trocar letra
        title.pack()

    #ANCHOR - Definição do subtitulo
    def subtitulo(self):
        subtitulo = Label(
            self.master,
            text="Feito em Python 3.12",
            font=("Helvetica", 10, "bold"),  # TODO Trocar letra
        )
        subtitulo.pack()
# !SECTION


# SECTION - Rodar a app
root = Tk()
app = App(root)
root.mainloop()
# !SECTION
