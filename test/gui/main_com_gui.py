# SECTION - Lista de Modulos
from tkinter import *  # ANCHOR - Modulo para criar a app
# !SECTION


# SECTION - Aolicação
class App:
    def __init__(self, master):
        self.master = master
        self.titulo()
        self.subtitulo()

    # ANCHOR -  Definição do titulo
    def titulo(self):
        title = Label(
            self.master, text="TO-DO Python", font=("Helvetica", 14, "bold")
        )  # TODO Trocar letra
        title.pack()

    # ANCHOR - Definição do subtitulo
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

root.title("TO-DO Python")
photo_1 = PhotoImage(file="assets/pixlr-logo-sem-fundo.png")
root.iconphoto(False, photo_1)
root.geometry("1280x800")
root.maxsize(1280, 800)

app = App(root)
root.mainloop()
# !SECTION
