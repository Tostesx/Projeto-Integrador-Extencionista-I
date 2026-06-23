import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime


def abrir_tela_principal():
    janela = tk.Tk()
    janela.title("Sistema Escolar IF3000")
    janela.geometry("900x650")
    janela.configure(bg="lightgreen")

    # Título
    tk.Label(
        janela,
        text="Bem-vindo ao Sistema Escolar IF3000",
        font=("Times New Roman", 18, "bold"),
        fg="darkgreen",
        bg="lightgreen"
    ).pack(pady=20)

    # ========== Notebook (abas) ==========
    style = ttk.Style()
    style.theme_use("clam")

    # Estilo das abas
    style.configure(
        "TNotebook",
        background="lightgreen",
        borderwidth=0
    )
    style.configure(
        "TNotebook.Tab",
        font=("Times New Roman", 13, "bold"),
        padding=[20, 8],
        background="#a8d5a2",
        foreground="darkgreen"
    )
    style.map(
        "TNotebook.Tab",
        background=[("selected", "darkgreen"), ("active", "#5a9e50")],
        foreground=[("selected", "white"), ("active", "white")]
    )

    notebook = ttk.Notebook(janela)
    notebook.pack(fill="both", expand=True, padx=30, pady=10)

    # ========== Estilo dos botões internos ==========
    def criar_botao(frame, texto, comando):
        return tk.Button(
            frame,
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

    # ========== ABA: Alunos ==========
    aba_alunos = tk.Frame(notebook, bg="lightgreen")
    notebook.add(aba_alunos, text="👨‍🎓  Alunos")

    tk.Label(aba_alunos, text="Gerenciamento de Alunos",
             font=("Times New Roman", 15, "bold"), fg="darkgreen", bg="lightgreen").pack(pady=20)

    def abrir_tela_aluno():
        janela.destroy()
        from alunos import tela_aluno
        tela_aluno.abrir_tela_aluno()

    criar_botao(aba_alunos, "Acessar Gerenciamento de Alunos", abrir_tela_aluno).pack(pady=15)

    # ========== ABA: Disciplinas ==========
    aba_disciplinas = tk.Frame(notebook, bg="lightgreen")
    notebook.add(aba_disciplinas, text="📚  Disciplinas")

    tk.Label(aba_disciplinas, text="Gerenciamento de Disciplinas",
             font=("Times New Roman", 15, "bold"), fg="darkgreen", bg="lightgreen").pack(pady=20)

    def abrir_tela_disciplina():
        janela.destroy()
        from disciplinas import tela_disciplina
        tela_disciplina.abrir_tela_disciplina()

    criar_botao(aba_disciplinas, "Acessar Gerenciamento de Disciplinas", abrir_tela_disciplina).pack(pady=15)

    # ========== ABA: Matrículas ==========
    aba_matriculas = tk.Frame(notebook, bg="lightgreen")
    notebook.add(aba_matriculas, text="📋  Matrículas")

    tk.Label(aba_matriculas, text="Gerenciamento de Matrículas",
             font=("Times New Roman", 15, "bold"), fg="darkgreen", bg="lightgreen").pack(pady=20)

    def abrir_tela_matricula():
        janela.destroy()
        from matriculas import tela_matricula
        tela_matricula.abrir_tela_matricula()

    criar_botao(aba_matriculas, "Acessar Gerenciamento de Matrículas", abrir_tela_matricula).pack(pady=15)

    # ========== Botão Sair do Sistema ==========
    tk.Button(
        janela,
        text="Sair do Sistema",
        font=("Times New Roman", 14, "bold"),
        fg="white",
        bg="#8b0000",
        activebackground="#cc0000",
        activeforeground="white",
        relief="raised",
        bd=3,
        cursor="hand2",
        width=20,
        command=janela.destroy
    ).pack(pady=20)

    janela.mainloop()


if __name__ == "__main__":
    abrir_tela_principal()
