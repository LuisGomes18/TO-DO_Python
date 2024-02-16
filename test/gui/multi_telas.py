from tkinter import *

class Application:
    def __init__(self, master):
        self.master = master
        self.menu()

    def criar_todo(self):
        self.destroy_window()
        self.master = Tk()
        label = Label(self.master, text='Criar')
        label.pack()
        self.master.geometry("600x600+250+50")
        menu_bt = Button(self.master, text='Voltar/Menu', command=self.menu)
        menu_bt.pack()

    def editar_todo(self):
        self.destroy_window()
        self.master = Tk()
        label = Label(self.master, text='Editar')
        label.pack()
        self.master.geometry("600x600+250+50")
        menu_bt = Button(self.master, text='Voltar/Menu', command=self.menu)
        menu_bt.pack()

    def menu(self):
        self.destroy_window()
        self.master = Tk()
        label = Label(self.master, text='Menu Principal')
        label.pack()

        menu_bt_criar = Button(self.master, text='Criar', command=self.criar_todo)
        menu_bt_editar = Button(self.master, text='Editar', command=self.editar_todo)

        menu_bt_criar.place(x=30, y=100)
        menu_bt_editar.place(x=30, y=130)

        self.master.geometry("600x600+250+50")
        self.master.title("Menu Principal")

    def destroy_window(self):
        try:
            self.master.destroy()
        except AttributeError:
            pass

def main():
    root = Tk()
    app = Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()
