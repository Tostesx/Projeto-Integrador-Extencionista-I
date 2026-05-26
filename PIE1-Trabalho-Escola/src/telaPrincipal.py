import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime
  

def abrir_tela_principal():
    janela = tk.Tk()
    janela.title("Sistema Escolar IF3000")
    janela.geometry("900x650")
    janela.configure(bg="lightgreen")

    label = tk.Label(janela, text="Bem-vindo ao Sistema Escolar IF3000", font=("New Times Roman", 18, "bold"), fg="darkgreen", bg="lightgreen")
    label.pack(pady=20)

    def abrir_tela_aluno():
        janela.destroy()
        from alunos import tela_aluno# Importa a tela de alunos
        tela_aluno.abrir_tela_aluno()

    botao_alunos = tk.Button(janela, text="Gerenciar Alunos", 
    font=("New Times Roman", 16, "bold"), fg="white", bg="darkgreen", command=abrir_tela_aluno)
    botao_alunos.pack(pady=40)

    def abrir_tela_disciplina():
        janela.destroy()
        from disciplinas import tela_disciplina # Importa a tela de disciplinas
        tela_disciplina.abrir_tela_disciplina()

    botao_disciplinas = tk.Button(janela, text="Gerenciar Disciplinas",
    font=("New Times Roman", 16, "bold"), fg="white", bg="darkgreen", command=abrir_tela_disciplina)
    botao_disciplinas.pack(pady=40)

    def abrir_tela_matricula():
        janela.destroy()
        from matriculas import tela_matricula # Importa a tela de matrículas
        tela_matricula.abrir_tela_matricula()

    botao_matriculas = tk.Button(janela, text="Gerenciar Matrículas",
    font=("New Times Roman", 16, "bold"), fg="white", bg="darkgreen", command=abrir_tela_matricula)
    botao_matriculas.pack(pady=40)

    botao_sair = tk.Button(janela, text="Sair do Sistema",
    font=("New Times Roman", 16, "bold"), fg="white", bg="darkgreen", command=janela.destroy)
    botao_sair.pack(pady=40)

    janela.mainloop()
if __name__ == "__main__":
    abrir_tela_principal()