import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

ARQUIVO_MATRICULAS = "matriculas_totais.csv"

def abrir_alterar_excluir():
    """Tela para alterar ou excluir uma matrícula existente"""
    # DICA: Carregue o CSV de matrículas em um DataFrame df.
    #       Também carregue alunos e disciplinas para mostrar nomes nos Comboboxes.
    
    janela = tk.Tk()
    janela.title("Alterar / Excluir Matrícula")
    janela.geometry("1000x700")
    janela.configure(bg="lightgreen")
    
    # Treeview para listar matrículas
    frame_tree = tk.Frame(janela)
    frame_tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    scrollbar = ttk.Scrollbar(frame_tree)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    colunas = ("ID_Matricula", "ID_Aluno", "ID_Disciplina", "Data", "Status", "Observacao")
    tree = ttk.Treeview(frame_tree, columns=colunas, show="headings",
                        yscrollcommand=scrollbar.set, height=10)
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=130, anchor="center")
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=tree.yview)
    
    # Frame com campos de edição
    frame_edicao = tk.Frame(janela, bg="lightgreen")
    frame_edicao.pack(pady=15)
    
    # DICA: Crie Comboboxes para selecionar aluno e disciplina (valores carregados dos CSVs)
    #       e Entry para status e observacao. A data pode ser editável ou automática.
    #       Use um IntVar para guardar o ID da matrícula selecionada.
    
    selected_id = tk.IntVar()
    
    def popular_treeview():
        # Limpa e recarrega a tree com os dados atuais do DataFrame df
        pass
    
    def ao_selecionar(event):
        # Quando clicar na tree, carregar os dados daquela matrícula nos campos
        pass
    
    def alterar_matricula():
        # Atualizar o registro no DataFrame e salvar CSV
        # Mostrar mensagem de sucesso e recarregar tree
        pass
    
    def excluir_matricula():
        # Remover a matrícula do DataFrame (df = df[df["ID_Matricula"] != selected_id.get()])
        # Salvar CSV, recarregar tree, limpar campos
        pass
    
    def limpar_campos():
        # Limpar os widgets de edição e resetar selected_id
        pass
    
    def voltar():
        janela.destroy()
        from matricula import tela_matricula
        tela_matricula.abrir_tela_matricula()
    
    # Botões (Alterar, Excluir, Limpar, Voltar)
    # frame_botoes = tk.Frame(janela, bg="lightgreen")
    # frame_botoes.pack(pady=10)
    # tk.Button(frame_botoes, text="Alterar", command=alterar_matricula).pack(side=tk.LEFT, padx=10)
    # tk.Button(frame_botoes, text="Excluir", command=excluir_matricula).pack(side=tk.LEFT, padx=10)
    # tk.Button(frame_botoes, text="Limpar", command=limpar_campos).pack(side=tk.LEFT, padx=10)
    # tk.Button(frame_botoes, text="Voltar", command=voltar).pack(side=tk.RIGHT, padx=10)
    
    popular_treeview()
    tree.bind("<<TreeviewSelect>>", ao_selecionar)
    janela.mainloop()

if __name__ == "__main__":
    abrir_alterar_excluir()