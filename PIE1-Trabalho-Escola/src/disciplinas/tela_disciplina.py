import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime

def abrir_tela_disciplina():
    """Tela principal de gerenciamento de disciplinas"""
    janela = tk.Tk()
    janela.title("Sistema Escolar IF3000 - Disciplinas")
    janela.geometry("900x650")
    janela.configure(bg="lightgreen")

    tk.Label(
        janela,
        text="Tela de Disciplinas",
        font=("Times New Roman", 18, "bold"),
        fg="darkgreen",
        bg="lightgreen"
    ).pack(pady=20)

    # ========== Funções de navegação ==========
    def cadastrar_disciplina():
        janela.destroy()
        from disciplinas import cadastra_disciplina
        cadastra_disciplina.cadastrar_disciplina()

    def abrir_consulta_disciplina():
        janela.destroy()
        from disciplinas import consulta_disciplina
        consulta_disciplina.abrir_consulta_disciplina()

    def abrir_alterar_excluir():
        janela.destroy()
        from disciplinas import alterar_excluir_d
        alterar_excluir_d.tela_alterar_excluir()

    def voltar_menu_principal():
        janela.destroy()
        import telaPrincipal
        telaPrincipal.abrir_tela_principal()

    # ========== Botões ==========
    def criar_botao(texto, comando):
        return tk.Button(
            janela,
            text=texto,
            font=("Times New Roman", 15, "bold"),
            fg="white",
            bg="darkgreen",
            activebackground="#5a9e50",
            activeforeground="white",
            relief="raised",
            bd=3,
            cursor="hand2",
            width=30,
            command=comando
        )

    criar_botao("Cadastrar Disciplina", cadastrar_disciplina).pack(pady=12)
    criar_botao("Lista de Disciplinas", abrir_consulta_disciplina).pack(pady=12)
    criar_botao("Alterar/Excluir Disciplina", abrir_alterar_excluir).pack(pady=12)

    # Botão voltar com estilo diferenciado
    tk.Button(
        janela,
        text="Voltar ao Menu Principal",
        font=("Times New Roman", 13, "bold"),
        fg="white",
        bg="#555555",
        activebackground="#333333",
        activeforeground="white",
        relief="raised",
        bd=3,
        cursor="hand2",
        width=25,
        command=voltar_menu_principal
    ).pack(pady=20)

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela_disciplina()