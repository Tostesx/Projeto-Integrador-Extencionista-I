import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime

def abrir_tela_aluno():
    janela = tk.Tk()
    janela.title("Sistema Escolar IF3000")
    janela.geometry("900x650")
    janela.configure(bg="lightgreen")

    label = tk.Label(janela, text="Tela de Alunos",
    font=("New Times Roman", 18, "bold"), fg="darkgreen", bg="lightgreen")
    label.pack(pady=20)

    def cadastrar_aluno():
        janela.destroy()
        from alunos import cadastra_aluno
        cadastra_aluno.cadastrar_aluno()

    botao_cadastra_aluno = tk.Button(janela, text="Cadastrar Aluno",
    font=("New Times Roman", 16, "bold"), fg="white", bg="darkgreen", command=cadastrar_aluno)
    botao_cadastra_aluno.pack(pady=40)

    def abrir_consulta_aluno():
        janela.destroy()
        from alunos import consulta_aluno
        consulta_aluno.abrir_consulta_aluno()

    botao_consulta_aluno = tk.Button(janela, text="Lista de Alunos",
    font=("New Times Roman", 16, "bold"), fg="white", bg="darkgreen", command=abrir_consulta_aluno)
    botao_consulta_aluno.pack(pady=40)

    def abrir_alterar_excluir():
        janela.destroy()
        from alunos import alterar_excluir
        alterar_excluir.tela_alterar_excluir()

    botao_exclui_aluno = tk.Button(janela, text="Alterar/Excluir Aluno", 
    font=("New Times Roman", 16, "bold"), fg="white", bg="darkgreen", command=abrir_alterar_excluir)
    botao_exclui_aluno.pack(pady=40)

    botao_matricula_aluno = tk.Button(janela, text="Matricular Aluno",
    font=("New Times Roman", 16, "bold"), fg="white", bg="darkgreen")

    def voltar_menu_principal():
        janela.destroy()
        import telaPrincipal
        telaPrincipal.abrir_tela_principal()

    botao_menu_principal = tk.Button(janela, text="Voltar ao Menu Principal",
    font=("New Times Roman", 16, "bold"), fg="white", bg="darkgreen", command=voltar_menu_principal)
    botao_menu_principal.pack(pady=40)

    janela.mainloop()
if __name__ == "__main__":    
    abrir_tela_aluno()