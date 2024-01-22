from tkinter import *
from tkinter import ttk


root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()

root.title('TO-DO APP')
root.geometry("400x200")

ttk.Label(frm, text="TO-DO App").grid(column=0, row=0)
ttk.Button(frm, text="Sair", command=root.destroy).grid(column=1, row=0)


root.mainloop()
