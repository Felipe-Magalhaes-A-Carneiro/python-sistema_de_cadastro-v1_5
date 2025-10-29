import tkinter as tk
import main
import cadastrar_emprestimo

def menu():
    
    tk.Label(main.janela, text = """       
    >>> MENU PRINCIPAL
    Esolha uma das opções abaixo:
              

    """).pack(pady=5)
    tk.Button(main.janela, text= "1- Cadastramento de empréstimos", command= cadastrar_emprestimo.cadastrar_emprestimo).pack(pady=2)

    tk.Button(main.janela, text= "2- Registro de empréstimos já cadastrados", command= cadastrar_emprestimo.cadastrar_emprestimo).pack(pady=2)

    tk.Button(main.janela, text= "3- Sair do sistema", command= exit()).pack(pady=2)


menu.mainloop()

    