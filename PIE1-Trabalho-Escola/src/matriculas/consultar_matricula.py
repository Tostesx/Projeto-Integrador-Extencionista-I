import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

ARQUIVO_MATRICULAS = "matriculas_totais.csv"

def abrir_consulta_matricula():
    """Exibe todas as matrículas em uma tabela com rolagem"""
    # DICA: Carregue o CSV para um DataFrame df.
    #       Junte (merge) com os DataFrames de alunos e disciplinas para mostrar
    #       o nome do aluno e o nome da disciplina ao invés dos IDs.
    #       Colunas sugeridas para exibição:
    #       ["ID Matrícula", "Aluno", "Disciplina", "Data", "Status", "Observação"]
    
    janela = tk.Tk()
    janela.title("Consulta de Matrículas")
    janela.geometry("1000x600")
    janela.configure(bg="lightgreen")
    
    tk.Label(janela, text="Matrículas Registradas", font=("Times New Roman", 18, "bold"),
             fg="darkgreen", bg="lightgreen").pack(pady=20)
    
    # Frame com scrollbar
    frame_tree = tk.Frame(janela)
    frame_tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    scrollbar = ttk.Scrollbar(frame_tree)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Definir colunas da Treeview
    colunas = ("ID_Matricula", "Aluno", "Disciplina", "Data", "Status", "Observacao")
    tree = ttk.Treeview(frame_tree, columns=colunas, show="headings",
                        yscrollcommand=scrollbar.set)
    
    # Configurar cabeçalhos e larguras
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=140, anchor="center")
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=tree.yview)
    
    # DICA: Preencher a tree com os dados do merge entre matrículas, alunos e disciplinas.
    #       Se não houver dados, exibir mensagem informativa.
    
    def voltar():
        janela.destroy()
        from matricula import tela_matricula
        tela_matricula.abrir_tela_matricula()
    
    tk.Button(janela, text="Voltar", font=("Times New Roman", 14),
              fg="white", bg="darkgreen", command=voltar).pack(pady=15)
    
    janela.mainloop()

if __name__ == "__main__":
    abrir_consulta_matricula()