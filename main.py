import tkinter as tk
from tkinter import messagebox
import menu_principal
#import cvs


root = tk.Tk()
root.title("SISTEMA DE CADASTRAMENTO DE LIVROS")
root.geometry('600x400+50+50')

tk.Label(root, text = """       
            
            BIBLIOTECA SENAI Morgan Figueiredo - Mooca
                SISTEMA DE CADASTRAMENTO DE LIVROS 
            ------------------------------------------
    """).pack(pady=10)

menubar = Menu(root)
root.config(menu=menubar)









root.mainloop()