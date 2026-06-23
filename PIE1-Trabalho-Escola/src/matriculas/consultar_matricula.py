import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

ARQUIVO_MATRICULAS = "matriculas_totais.csv"
ARQUIVO_ALUNOS = "alunos_totais.csv"
ARQUIVO_DISCIPLINAS = "disciplinas_totais.csv"

def abrir_consulta_matricula():
    """Exibe todas as matrículas em uma tabela com rolagem"""
    
    # ========== 1. Carregar dados ==========
    # Carregar matrículas
    if os.path.exists(ARQUIVO_MATRICULAS):
        df_matriculas = pd.read_csv(ARQUIVO_MATRICULAS)
    else:
        df_matriculas = pd.DataFrame(columns=["ID_Matricula", "ID_Aluno", "ID_Disciplina", 
                                              "Data_Matricula", "Status", "Observacao"])
    
    # Carregar alunos (para obter nomes)
    if os.path.exists(ARQUIVO_ALUNOS):
        df_alunos = pd.read_csv(ARQUIVO_ALUNOS)
        # Garantir colunas necessárias
        if "ID" not in df_alunos.columns or "Nome" not in df_alunos.columns:
            df_alunos = pd.DataFrame(columns=["ID", "Nome"])
    else:
        df_alunos = pd.DataFrame(columns=["ID", "Nome"])
    
    # Carregar disciplinas (para obter nomes)
    if os.path.exists(ARQUIVO_DISCIPLINAS):
        df_disciplinas = pd.read_csv(ARQUIVO_DISCIPLINAS)
        if "ID" not in df_disciplinas.columns or "Nome" not in df_disciplinas.columns:
            df_disciplinas = pd.DataFrame(columns=["ID", "Nome"])
    else:
        df_disciplinas = pd.DataFrame(columns=["ID", "Nome"])
    
    # ========== 2. Fazer merge para obter nomes ==========
    if not df_matriculas.empty:
        # Merge com alunos
        df_merged = df_matriculas.merge(df_alunos[["ID", "Nome"]], 
                                        left_on="ID_Aluno", right_on="ID", how="left")
        df_merged.rename(columns={"Nome": "Nome_Aluno"}, inplace=True)
        df_merged.drop(columns=["ID"], inplace=True, errors="ignore")
        
        # Merge com disciplinas
        df_merged = df_merged.merge(df_disciplinas[["ID", "Nome"]], 
                                    left_on="ID_Disciplina", right_on="ID", how="left")
        df_merged.rename(columns={"Nome": "Nome_Disciplina"}, inplace=True)
        df_merged.drop(columns=["ID"], inplace=True, errors="ignore")
        
        # Substituir NaN por "Não encontrado" (caso algum merge falhe)
        df_merged["Nome_Aluno"] = df_merged["Nome_Aluno"].fillna("Aluno não encontrado")
        df_merged["Nome_Disciplina"] = df_merged["Nome_Disciplina"].fillna("Disciplina não encontrada")
    else:
        df_merged = df_matriculas.copy()
        df_merged["Nome_Aluno"] = ""
        df_merged["Nome_Disciplina"] = ""
    
    # ========== 3. Interface Gráfica ==========
    janela = tk.Tk()
    janela.title("Consulta de Matrículas - Sistema Escolar IF3000")
    janela.geometry("1100x650")
    janela.configure(bg="lightgreen")
    
    tk.Label(janela, text="Matrículas Registradas", font=("Times New Roman", 18, "bold"),
             fg="darkgreen", bg="lightgreen").pack(pady=20)
    
    # Frame com scrollbar
    frame_tree = tk.Frame(janela, bg="lightgreen")
    frame_tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    scrollbar = ttk.Scrollbar(frame_tree)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Definir colunas da Treeview
    colunas = ("ID_Matricula", "Aluno", "Disciplina", "Data", "Status", "Observacao")
    tree = ttk.Treeview(frame_tree, columns=colunas, show="headings",
                        yscrollcommand=scrollbar.set, height=15)
    
    # Configurar cabeçalhos e larguras
    for col in colunas:
        tree.heading(col, text=col)
        if col == "ID_Matricula":
            tree.column(col, width=80, anchor="center")
        elif col in ["Aluno", "Disciplina"]:
            tree.column(col, width=200, anchor="w")
        elif col == "Data":
            tree.column(col, width=100, anchor="center")
        elif col == "Status":
            tree.column(col, width=100, anchor="center")
        elif col == "Observacao":
            tree.column(col, width=200, anchor="w")
        else:
            tree.column(col, width=120, anchor="center")
    
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=tree.yview)
    
    # ========== 4. Função para popular a Treeview ==========
    def popular_treeview():
        """Preenche a Treeview com os dados do merge."""
        for item in tree.get_children():
            tree.delete(item)
        
        if df_merged.empty:
            # Exibir mensagem na Treeview (não há dados)
            tree.insert("", tk.END, values=("", "Nenhuma matrícula cadastrada", "", "", "", ""))
            # Ajustar visualmente: centralizar a mensagem
            tree.column("Aluno", width=400, anchor="center")
            return
        
        # Inserir cada linha
        for _, row in df_merged.iterrows():
            tree.insert("", tk.END, values=(
                row.get("ID_Matricula", ""),
                row.get("Nome_Aluno", ""),
                row.get("Nome_Disciplina", ""),
                row.get("Data_Matricula", ""),
                row.get("Status", ""),
                row.get("Observacao", "")
            ))
    
    # ========== 5. Função Voltar ==========
    def voltar():
        janela.destroy()
        from matriculas import tela_matricula
        tela_matricula.abrir_tela_matricula()
    
    # ========== 6. Botões ==========
    frame_botoes = tk.Frame(janela, bg="lightgreen")
    frame_botoes.pack(pady=15)
    
    # Botão para atualizar (recarregar dados)
    def atualizar():
        """Recarrega os dados e atualiza a Treeview."""
        nonlocal df_merged
        # Recarregar dados
        if os.path.exists(ARQUIVO_MATRICULAS):
            df_matriculas = pd.read_csv(ARQUIVO_MATRICULAS)
        else:
            df_matriculas = pd.DataFrame(columns=["ID_Matricula", "ID_Aluno", "ID_Disciplina", 
                                                  "Data_Matricula", "Status", "Observacao"])
        if os.path.exists(ARQUIVO_ALUNOS):
            df_alunos = pd.read_csv(ARQUIVO_ALUNOS)
        else:
            df_alunos = pd.DataFrame(columns=["ID", "Nome"])
        if os.path.exists(ARQUIVO_DISCIPLINAS):
            df_disciplinas = pd.read_csv(ARQUIVO_DISCIPLINAS)
        else:
            df_disciplinas = pd.DataFrame(columns=["ID", "Nome"])
        
        # Refazer merge
        if not df_matriculas.empty:
            df_merged = df_matriculas.merge(df_alunos[["ID", "Nome"]], 
                                            left_on="ID_Aluno", right_on="ID", how="left")
            df_merged.rename(columns={"Nome": "Nome_Aluno"}, inplace=True)
            df_merged.drop(columns=["ID"], inplace=True, errors="ignore")
            df_merged = df_merged.merge(df_disciplinas[["ID", "Nome"]], 
                                        left_on="ID_Disciplina", right_on="ID", how="left")
            df_merged.rename(columns={"Nome": "Nome_Disciplina"}, inplace=True)
            df_merged.drop(columns=["ID"], inplace=True, errors="ignore")
            df_merged["Nome_Aluno"] = df_merged["Nome_Aluno"].fillna("Aluno não encontrado")
            df_merged["Nome_Disciplina"] = df_merged["Nome_Disciplina"].fillna("Disciplina não encontrada")
        else:
            df_merged = df_matriculas.copy()
            df_merged["Nome_Aluno"] = ""
            df_merged["Nome_Disciplina"] = ""
        
        popular_treeview()
        messagebox.showinfo("Atualizado", "Dados recarregados com sucesso!")
    
    botao_atualizar = tk.Button(frame_botoes, text="Atualizar", font=("Times New Roman", 14),
                                fg="white", bg="blue", command=atualizar)
    botao_atualizar.pack(side=tk.LEFT, padx=20)
    
    botao_voltar = tk.Button(frame_botoes, text="Voltar", font=("Times New Roman", 14),
                             fg="white", bg="darkgreen", command=voltar)
    botao_voltar.pack(side=tk.RIGHT, padx=20)
    
    # ========== 7. Popular a Treeview e iniciar ==========
    popular_treeview()
    janela.mainloop()

if __name__ == "__main__":
    abrir_consulta_matricula()