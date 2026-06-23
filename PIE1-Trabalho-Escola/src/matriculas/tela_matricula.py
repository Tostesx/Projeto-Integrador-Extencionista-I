import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd


def abrir_tela_matricula():
    """Tela principal de gerenciamento de matrículas"""
    janela = tk.Tk()
    janela.title("Sistema Escolar IF3000 - Matrículas")
    janela.geometry("900x650")
    janela.configure(bg="lightgreen")

    tk.Label(
        janela,
        text="Tela de Matrículas",
        font=("Times New Roman", 18, "bold"),
        fg="darkgreen",
        bg="lightgreen"
    ).pack(pady=20)

    # ========== Funções de navegação ==========
    def matricular_aluno():
        janela.destroy()
        from matriculas import matricular_aluno as mat
        mat.abrir_matricular_aluno()

    def consultar_matriculas():
        janela.destroy()
        from matriculas import consultar_matricula
        consultar_matricula.abrir_consulta_matricula()

    def alterar_excluir_matricula():
        janela.destroy()
        from matriculas import alterar_excluir_m
        alterar_excluir_m.abrir_alterar_excluir()

    def voltar_menu():
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

    criar_botao("Matricular Aluno", matricular_aluno).pack(pady=12)
    criar_botao("Consultar Matrículas", consultar_matriculas).pack(pady=12)
    criar_botao("Alterar/Excluir Matrícula", alterar_excluir_matricula).pack(pady=12)

    # Botão voltar com estilo diferenciado
    tk.Button(
        janela,
        text="Voltar ao Menu",
        font=("Times New Roman", 13, "bold"),
        fg="white",
        bg="#555555",
        activebackground="#333333",
        activeforeground="white",
        relief="raised",
        bd=3,
        cursor="hand2",
        width=20,
        command=voltar_menu
    ).pack(pady=20)

    janela.mainloop()


if __name__ == "__main__":
    abrir_tela_matricula()
