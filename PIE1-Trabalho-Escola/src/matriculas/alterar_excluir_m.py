import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
from datetime import datetime

ARQUIVO_MATRICULAS = "matriculas_totais.csv"
ARQUIVO_ALUNOS = "alunos_totais.csv"
ARQUIVO_DISCIPLINAS = "disciplinas_totais.csv"

def abrir_alterar_excluir():
    """Tela para alterar ou excluir uma matrícula existente"""
    
    # ========== 1. Carregar dados ==========
    # Matrículas
    if os.path.exists(ARQUIVO_MATRICULAS):
        df = pd.read_csv(ARQUIVO_MATRICULAS)
        colunas_esperadas = ["ID_Matricula", "ID_Aluno", "ID_Disciplina", "Data_Matricula", "Status", "Observacao"]
        if df.empty or not all(col in df.columns for col in colunas_esperadas):
            df = pd.DataFrame(columns=colunas_esperadas)
    else:
        df = pd.DataFrame(columns=["ID_Matricula", "ID_Aluno", "ID_Disciplina", "Data_Matricula", "Status", "Observacao"])
    
    # Alunos (para nomes)
    if os.path.exists(ARQUIVO_ALUNOS):
        df_alunos = pd.read_csv(ARQUIVO_ALUNOS)
        if "ID" not in df_alunos.columns or "Nome" not in df_alunos.columns:
            df_alunos = pd.DataFrame(columns=["ID", "Nome"])
    else:
        df_alunos = pd.DataFrame(columns=["ID", "Nome"])
    
    # Disciplinas (para nomes)
    if os.path.exists(ARQUIVO_DISCIPLINAS):
        df_disciplinas = pd.read_csv(ARQUIVO_DISCIPLINAS)
        if "ID" not in df_disciplinas.columns or "Nome" not in df_disciplinas.columns:
            df_disciplinas = pd.DataFrame(columns=["ID", "Nome"])
    else:
        df_disciplinas = pd.DataFrame(columns=["ID", "Nome"])
    
    # Listas para Comboboxes (formato "ID - Nome")
    lista_alunos = [f"{row['ID']} - {row['Nome']}" for _, row in df_alunos.iterrows()]
    lista_disciplinas = [f"{row['ID']} - {row['Nome']}" for _, row in df_disciplinas.iterrows()]
    
    # ========== 2. Interface Gráfica ==========
    janela = tk.Tk()
    janela.title("Alterar / Excluir Matrícula - Sistema Escolar IF3000")
    janela.geometry("1100x750")
    janela.configure(bg="lightgreen")
    
    tk.Label(janela, text="Alterar / Excluir Matrícula", font=("Times New Roman", 18, "bold"),
             fg="darkgreen", bg="lightgreen").pack(pady=15)
    
    # Treeview (com scroll)
    frame_tree = tk.Frame(janela)
    frame_tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    scrollbar = ttk.Scrollbar(frame_tree)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Colunas da tree (exibindo IDs e nomes dos alunos/disciplinas via merge)
    colunas_tree = ("ID_Matricula", "ID_Aluno", "Aluno", "ID_Disciplina", "Disciplina", "Data", "Status", "Observacao")
    tree = ttk.Treeview(frame_tree, columns=colunas_tree, show="headings",
                        yscrollcommand=scrollbar.set, height=8)
    for col in colunas_tree:
        tree.heading(col, text=col)
        if col in ["ID_Matricula", "ID_Aluno", "ID_Disciplina"]:
            tree.column(col, width=80, anchor="center")
        elif col in ["Data", "Status"]:
            tree.column(col, width=100, anchor="center")
        elif col == "Observacao":
            tree.column(col, width=200, anchor="w")
        else:  # Aluno, Disciplina
            tree.column(col, width=180, anchor="w")
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=tree.yview)
    
    # ========== 3. Frame de edição ==========
    frame_edicao = tk.Frame(janela, bg="lightgreen")
    frame_edicao.pack(pady=15)
    
    # Campos: Aluno (Combobox)
    tk.Label(frame_edicao, text="Aluno:", font=("Times New Roman", 14), bg="lightgreen").grid(row=0, column=0, sticky="e", padx=10, pady=5)
    combo_aluno = ttk.Combobox(frame_edicao, values=lista_alunos, font=("Times New Roman", 12), width=50)
    combo_aluno.grid(row=0, column=1, padx=10, pady=5)
    combo_aluno.set("")
    
    # Disciplina (Combobox)
    tk.Label(frame_edicao, text="Disciplina:", font=("Times New Roman", 14), bg="lightgreen").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    combo_disciplina = ttk.Combobox(frame_edicao, values=lista_disciplinas, font=("Times New Roman", 12), width=50)
    combo_disciplina.grid(row=1, column=1, padx=10, pady=5)
    combo_disciplina.set("")
    
    # Data (Entry editável)
    tk.Label(frame_edicao, text="Data (dd/mm/aaaa):", font=("Times New Roman", 14), bg="lightgreen").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entry_data = tk.Entry(frame_edicao, font=("Times New Roman", 12), width=30)
    entry_data.grid(row=2, column=1, padx=10, pady=5, sticky="w")
    
    # Status (Combobox fixo)
    tk.Label(frame_edicao, text="Status:", font=("Times New Roman", 14), bg="lightgreen").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    combo_status = ttk.Combobox(frame_edicao, values=["Ativo", "Trancado", "Concluído"], font=("Times New Roman", 12), width=30)
    combo_status.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    combo_status.set("Ativo")
    
    # Observação (Entry)
    tk.Label(frame_edicao, text="Observação:", font=("Times New Roman", 14), bg="lightgreen").grid(row=4, column=0, sticky="e", padx=10, pady=5)
    entry_obs = tk.Entry(frame_edicao, font=("Times New Roman", 12), width=50)
    entry_obs.grid(row=4, column=1, padx=10, pady=5)
    
    # ID selecionado
    selected_id = tk.IntVar()
    
    # ========== 4. Funções ==========
    def popular_treeview():
        """Preenche a treeview com dados do DataFrame df (matrículas) + nomes de alunos e disciplinas"""
        for item in tree.get_children():
            tree.delete(item)
        
        if df.empty:
            tree.insert("", tk.END, values=("", "", "Nenhuma matrícula cadastrada", "", "", "", "", ""))
            return
        
        # Merge com alunos e disciplinas para obter nomes
        df_merged = df.merge(df_alunos[["ID", "Nome"]], left_on="ID_Aluno", right_on="ID", how="left")
        df_merged.rename(columns={"Nome": "Nome_Aluno"}, inplace=True)
        df_merged.drop(columns=["ID"], inplace=True, errors="ignore")
        
        df_merged = df_merged.merge(df_disciplinas[["ID", "Nome"]], left_on="ID_Disciplina", right_on="ID", how="left")
        df_merged.rename(columns={"Nome": "Nome_Disciplina"}, inplace=True)
        df_merged.drop(columns=["ID"], inplace=True, errors="ignore")
        
        df_merged["Nome_Aluno"] = df_merged["Nome_Aluno"].fillna("Aluno não encontrado")
        df_merged["Nome_Disciplina"] = df_merged["Nome_Disciplina"].fillna("Disciplina não encontrada")
        
        for _, row in df_merged.iterrows():
            tree.insert("", tk.END, values=(
                row["ID_Matricula"],
                row["ID_Aluno"],
                row["Nome_Aluno"],
                row["ID_Disciplina"],
                row["Nome_Disciplina"],
                row["Data_Matricula"],
                row["Status"],
                row["Observacao"]
            ))
    
    def ao_selecionar(event):
        """Quando uma linha é selecionada, carrega os dados nos campos de edição"""
        selecionado = tree.selection()
        if not selecionado:
            return
        valores = tree.item(selecionado[0])['values']
        if not valores or len(valores) < 8:
            return
        # ID_Matricula, ID_Aluno, Nome_Aluno, ID_Disciplina, Nome_Disciplina, Data, Status, Obs
        selected_id.set(valores[0])
        # Carregar combos com "ID - Nome" – precisamos montar a string
        id_aluno = valores[1]
        nome_aluno = valores[2]
        if id_aluno != "" and nome_aluno != "Aluno não encontrado":
            combo_aluno.set(f"{id_aluno} - {nome_aluno}")
        else:
            combo_aluno.set("")
        
        id_disciplina = valores[3]
        nome_disciplina = valores[4]
        if id_disciplina != "" and nome_disciplina != "Disciplina não encontrada":
            combo_disciplina.set(f"{id_disciplina} - {nome_disciplina}")
        else:
            combo_disciplina.set("")
        
        entry_data.delete(0, tk.END)
        entry_data.insert(0, valores[5])
        
        combo_status.set(valores[6])
        
        entry_obs.delete(0, tk.END)
        entry_obs.insert(0, valores[7] if valores[7] is not None else "")
    
    def limpar_campos():
        """Limpa todos os campos de edição e desmarca a seleção"""
        combo_aluno.set("")
        combo_disciplina.set("")
        entry_data.delete(0, tk.END)
        combo_status.set("Ativo")
        entry_obs.delete(0, tk.END)
        selected_id.set(0)
        for item in tree.selection():
            tree.selection_remove(item)
    
    def alterar_matricula():
        nonlocal df
        if selected_id.get() == 0:
            messagebox.showerror("Erro", "Selecione uma matrícula para alterar.")
            return
        
        # Coletar dados dos campos
        aluno_sel = combo_aluno.get().strip()
        disciplina_sel = combo_disciplina.get().strip()
        data = entry_data.get().strip()
        status = combo_status.get().strip()
        obs = entry_obs.get().strip()
        
        # Validações
        if not aluno_sel:
            messagebox.showerror("Erro", "Selecione um aluno.")
            return
        if not disciplina_sel:
            messagebox.showerror("Erro", "Selecione uma disciplina.")
            return
        if not data:
            messagebox.showerror("Erro", "Informe a data da matrícula.")
            return
        if status not in ["Ativo", "Trancado", "Concluído"]:
            messagebox.showerror("Erro", "Status inválido.")
            return
        
        # Extrair IDs
        try:
            id_aluno = int(aluno_sel.split(" - ")[0])
        except ValueError:
            messagebox.showerror("Erro", "Aluno inválido.")
            return
        try:
            id_disciplina = int(disciplina_sel.split(" - ")[0])
        except ValueError:
            messagebox.showerror("Erro", "Disciplina inválida.")
            return
        
        # Verificar se os IDs existem nos DataFrames carregados
        if id_aluno not in df_alunos["ID"].values:
            messagebox.showerror("Erro", "Aluno não encontrado na base.")
            return
        if id_disciplina not in df_disciplinas["ID"].values:
            messagebox.showerror("Erro", "Disciplina não encontrada na base.")
            return
        
        # Atualizar o DataFrame
        idx = df[df["ID_Matricula"] == selected_id.get()].index
        if len(idx) == 0:
            messagebox.showerror("Erro", "Matrícula não encontrada.")
            return
        idx = idx[0]
        
        df.at[idx, "ID_Aluno"] = id_aluno
        df.at[idx, "ID_Disciplina"] = id_disciplina
        df.at[idx, "Data_Matricula"] = data
        df.at[idx, "Status"] = status
        df.at[idx, "Observacao"] = obs
        
        # Salvar
        df.to_csv(ARQUIVO_MATRICULAS, index=False, encoding='utf-8-sig')
        
        popular_treeview()
        limpar_campos()
        messagebox.showinfo("Sucesso", f"Matrícula ID {selected_id.get()} alterada com sucesso!")
    
    def excluir_matricula():
        nonlocal df
        if selected_id.get() == 0:
            messagebox.showerror("Erro", "Selecione uma matrícula para excluir.")
            return
        if not messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir esta matrícula?"):
            return
        
        df = df[df["ID_Matricula"] != selected_id.get()]
        df.to_csv(ARQUIVO_MATRICULAS, index=False, encoding='utf-8-sig')
        popular_treeview()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Matrícula excluída com sucesso!")
    
    def voltar():
        janela.destroy()
        from matriculas import tela_matricula
        tela_matricula.abrir_tela_matricula()
    
    # ========== 5. Botões ==========
    frame_botoes = tk.Frame(janela, bg="lightgreen")
    frame_botoes.pack(pady=15)
    
    btn_alterar = tk.Button(frame_botoes, text="Alterar", font=("Times New Roman", 14),
                            fg="white", bg="darkgreen", command=alterar_matricula)
    btn_alterar.pack(side=tk.LEFT, padx=15)
    
    btn_excluir = tk.Button(frame_botoes, text="Excluir", font=("Times New Roman", 14),
                            fg="white", bg="darkred", command=excluir_matricula)
    btn_excluir.pack(side=tk.LEFT, padx=15)
    
    btn_limpar = tk.Button(frame_botoes, text="Limpar", font=("Times New Roman", 14),
                           fg="white", bg="gray", command=limpar_campos)
    btn_limpar.pack(side=tk.LEFT, padx=15)
    
    btn_voltar = tk.Button(frame_botoes, text="Voltar", font=("Times New Roman", 14),
                           fg="white", bg="darkgreen", command=voltar)
    btn_voltar.pack(side=tk.RIGHT, padx=15)
    
    # ========== 6. Inicialização ==========
    popular_treeview()
    tree.bind("<<TreeviewSelect>>", ao_selecionar)
    
    janela.mainloop()

if __name__ == "__main__":
    abrir_alterar_excluir()