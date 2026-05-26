import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

ARQUIVO_ALUNOS = "alunos_totais.csv"

def abrir_consulta_aluno():
    # Carregar dados do CSV
    if os.path.exists(ARQUIVO_ALUNOS):
        df = pd.read_csv(ARQUIVO_ALUNOS)
        # Garantir colunas
        if df.empty or not all(col in df.columns for col in ["ID", "Nome", "Idade", "CPF", "Telefone", "Email"]):
            df = pd.DataFrame(columns=["ID", "Nome", "Idade", "CPF", "Telefone", "Email"])
    else:
        df = pd.DataFrame(columns=["ID", "Nome", "Idade", "CPF", "Telefone", "Email"])

    janela = tk.Tk()
    janela.title("Consulta de Alunos - Sistema Escolar IF3000")
    janela.geometry("900x650")
    janela.configure(bg="lightgreen")

    # Título
    titulo = tk.Label(janela, text="Lista de Alunos Cadastrados", font=("Times New Roman", 18, "bold"),
                      fg="darkgreen", bg="lightgreen")
    titulo.pack(pady=20)

    # Frame com scrollbar para a Treeview
    frame_tree = tk.Frame(janela)
    frame_tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    scrollbar = ttk.Scrollbar(frame_tree)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    colunas = ("ID", "Nome", "Idade", "CPF", "Telefone", "Email")
    tree = ttk.Treeview(frame_tree, columns=colunas, show="headings", height=15,
                        yscrollcommand=scrollbar.set)
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=tree.yview)

    # Inserir dados
    for _, row in df.iterrows():
        tree.insert("", tk.END, values=(
            row["ID"], row["Nome"], row["Idade"],
            row["CPF"], row["Telefone"], row["Email"]
        ))

    # Se não houver dados, mostrar mensagem
    if df.empty:
        # Insere uma linha informativa (opcional)
        tree.insert("", tk.END, values=("", "Nenhum aluno cadastrado", "", "", "", ""))

    # Botão voltar
    def voltar():
        janela.destroy()
        from alunos import tela_aluno
        tela_aluno.abrir_tela_aluno()

    botao_voltar = tk.Button(janela, text="Voltar", font=("Times New Roman", 14),
                             fg="white", bg="darkgreen", command=voltar)
    botao_voltar.pack(pady=15)

    janela.mainloop()

if __name__ == "__main__":
    abrir_consulta_aluno()