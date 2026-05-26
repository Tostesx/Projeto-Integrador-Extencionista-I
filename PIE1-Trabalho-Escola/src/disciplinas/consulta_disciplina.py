import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

ARQUIVO_DISCIPLINAS = "disciplinas_totais.csv"

def abrir_consulta_disciplina():
    # Carregar dados do CSV
    if os.path.exists(ARQUIVO_DISCIPLINAS):
        df = pd.read_csv(ARQUIVO_DISCIPLINAS)
        # Garantir colunas
        if df.empty or not all(col in df.columns for col in ["ID", "Nome", "CargaHoraria", "Professor", "Curso"]):
            df = pd.DataFrame(columns=["ID", "Nome", "CargaHoraria", "Professor", "Curso"])
    else:
        df = pd.DataFrame(columns=["ID", "Nome", "CargaHoraria", "Professor", "Curso"])

    janela = tk.Tk()
    janela.title("Consulta de Disciplinas - Sistema Escolar IF3000")
    janela.geometry("900x650")
    janela.configure(bg="lightgreen")

    # Título
    titulo = tk.Label(janela, text="Lista de Disciplinas Cadastradas", font=("Times New Roman", 18, "bold"),
                      fg="darkgreen", bg="lightgreen")
    titulo.pack(pady=20)

    # Frame com scrollbar para a Treeview
    frame_tree = tk.Frame(janela)
    frame_tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    scrollbar = ttk.Scrollbar(frame_tree)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    colunas = ("ID", "Nome", "Carga Horária", "Professor", "Curso")
    tree = ttk.Treeview(frame_tree, columns=colunas, show="headings", height=15,
                        yscrollcommand=scrollbar.set)
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=tree.yview)

    # Inserir dados
    for _, row in df.iterrows():
        tree.insert("", tk.END, values=(
            row["ID"], row["Nome"], row["CargaHoraria"],
            row["Professor"], row["Curso"]
        ))

    # Se não houver dados, mostrar mensagem
    if df.empty:
        tree.insert("", tk.END, values=("", "Nenhuma disciplina cadastrada", "", "", ""))

    # Botão voltar
    def voltar():
        janela.destroy()
        from disciplinas import tela_disciplina  # ajuste conforme sua estrutura
        tela_disciplina.abrir_tela_disciplina()

    botao_voltar = tk.Button(janela, text="Voltar", font=("Times New Roman", 14),
                             fg="white", bg="darkgreen", command=voltar)
    botao_voltar.pack(pady=15)

    janela.mainloop()

if __name__ == "__main__":
    abrir_consulta_disciplina()