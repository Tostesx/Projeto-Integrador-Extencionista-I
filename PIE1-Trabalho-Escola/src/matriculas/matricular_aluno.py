import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
from datetime import datetime

# Arquivo CSV que armazenará as matrículas
ARQUIVO_MATRICULAS = "matriculas_totais.csv"


def abrir_matricular_aluno():
    """
    Tela para realizar uma nova matrícula.
    Carrega os dados de alunos e disciplinas para preencher Comboboxes.
    """
    # ========== 1. Carregar dados de matrículas (para ID e Treeview) ==========
    if os.path.exists(ARQUIVO_MATRICULAS):
        df_matriculas = pd.read_csv(ARQUIVO_MATRICULAS)
        colunas_esperadas = ["ID_Matricula", "ID_Aluno", "ID_Disciplina", "Data_Matricula", "Status", "Observacao"]
        if df_matriculas.empty or not all(col in df_matriculas.columns for col in colunas_esperadas):
            df_matriculas = pd.DataFrame(columns=colunas_esperadas)
    else:
        df_matriculas = pd.DataFrame(columns=["ID_Matricula", "ID_Aluno", "ID_Disciplina", "Data_Matricula", "Status", "Observacao"])

    if not df_matriculas.empty:
        proximo_id = df_matriculas["ID_Matricula"].max() + 1
    else:
        proximo_id = 1

    # ========== 2. Carregar listas de alunos e disciplinas ==========
    if os.path.exists("alunos_totais.csv"):
        df_alunos = pd.read_csv("alunos_totais.csv")
        lista_alunos = [f"{row['ID']} - {row['Nome']}" for _, row in df_alunos.iterrows()]
    else:
        lista_alunos = []
        df_alunos = pd.DataFrame(columns=["ID", "Nome"])

    if os.path.exists("disciplinas_totais.csv"):
        df_disciplinas = pd.read_csv("disciplinas_totais.csv")
        lista_disciplinas = [f"{row['ID']} - {row['Nome']}" for _, row in df_disciplinas.iterrows()]
    else:
        lista_disciplinas = []
        df_disciplinas = pd.DataFrame(columns=["ID", "Nome"])

    # ========== 3. Interface Gráfica ==========
    janela = tk.Tk()
    janela.title("Matricular Aluno - Sistema Escolar IF3000")
    janela.geometry("900x700")
    janela.configure(bg="lightgreen")

    tk.Label(janela, text="Nova Matrícula", font=("Times New Roman", 18, "bold"),
             fg="darkgreen", bg="lightgreen").grid(row=0, column=0, columnspan=2, pady=20)

    frame = tk.Frame(janela, bg="lightgreen")
    frame.grid(row=1, column=0, padx=20, pady=10, sticky="n")

    # ========== 4. Campos do formulário ==========
    tk.Label(frame, text="Aluno:", font=("Times New Roman", 14), bg="lightgreen").grid(row=0, column=0, sticky="e", padx=10, pady=5)
    combo_aluno = ttk.Combobox(frame, values=lista_alunos, font=("Times New Roman", 12), width=50)
    combo_aluno.grid(row=0, column=1, padx=10, pady=5)
    combo_aluno.set("")

    tk.Label(frame, text="Disciplina:", font=("Times New Roman", 14), bg="lightgreen").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    combo_disciplina = ttk.Combobox(frame, values=lista_disciplinas, font=("Times New Roman", 12), width=50)
    combo_disciplina.grid(row=1, column=1, padx=10, pady=5)
    combo_disciplina.set("")

    tk.Label(frame, text="Status:", font=("Times New Roman", 14), bg="lightgreen").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    combo_status = ttk.Combobox(frame, values=["Ativo", "Trancado", "Concluído"], font=("Times New Roman", 12), width=30)
    combo_status.grid(row=2, column=1, padx=10, pady=5)
    combo_status.set("Ativo")

    tk.Label(frame, text="Observação:", font=("Times New Roman", 14), bg="lightgreen").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entry_obs = tk.Entry(frame, font=("Times New Roman", 12), width=50)
    entry_obs.grid(row=3, column=1, padx=10, pady=5)

    data_atual = datetime.now().strftime("%d/%m/%Y")
    tk.Label(frame, text=f"Data: {data_atual}", font=("Times New Roman", 12, "bold"),
             bg="lightgreen", fg="darkgreen").grid(row=4, column=0, columnspan=2, pady=5)

    # ========== 5. Treeview ==========
    colunas_tree = ("ID_Matricula", "ID_Aluno", "Aluno", "ID_Disciplina", "Disciplina", "Data", "Status", "Obs")
    tree_matriculas = ttk.Treeview(janela, columns=colunas_tree, show="headings", height=6)
    for col in colunas_tree:
        tree_matriculas.heading(col, text=col)
        if col in ["ID_Matricula", "ID_Aluno", "ID_Disciplina"]:
            tree_matriculas.column(col, width=80, anchor="center")
        elif col in ["Data", "Status"]:
            tree_matriculas.column(col, width=100, anchor="center")
        elif col == "Obs":
            tree_matriculas.column(col, width=150, anchor="w")
        else:
            tree_matriculas.column(col, width=180, anchor="w")
    tree_matriculas.grid(row=2, column=0, pady=20, padx=20, sticky="ew")

    # ========== 6. Funções ==========
    def atualizar_treeview():
        for item in tree_matriculas.get_children():
            tree_matriculas.delete(item)
        if os.path.exists(ARQUIVO_MATRICULAS):
            df_temp = pd.read_csv(ARQUIVO_MATRICULAS)
            for _, row in df_temp.iterrows():
                id_aluno = row["ID_Aluno"]
                id_disciplina = row["ID_Disciplina"]
                nome_aluno = df_alunos[df_alunos["ID"] == id_aluno]["Nome"].values[0] if not df_alunos.empty and id_aluno in df_alunos["ID"].values else "Desconhecido"
                nome_disciplina = df_disciplinas[df_disciplinas["ID"] == id_disciplina]["Nome"].values[0] if not df_disciplinas.empty and id_disciplina in df_disciplinas["ID"].values else "Desconhecido"
                tree_matriculas.insert("", tk.END, values=(
                    row["ID_Matricula"], row["ID_Aluno"], nome_aluno,
                    row["ID_Disciplina"], nome_disciplina,
                    row["Data_Matricula"], row["Status"], row["Observacao"]
                ))

    def limpar_campos():
        combo_aluno.set("")
        combo_disciplina.set("")
        combo_status.set("Ativo")
        entry_obs.delete(0, tk.END)

    def salvar_matricula():
        nonlocal df_matriculas, proximo_id

        aluno_selecionado = combo_aluno.get().strip()
        disciplina_selecionada = combo_disciplina.get().strip()
        status = combo_status.get().strip()
        observacao = entry_obs.get().strip()

        if not aluno_selecionado:
            messagebox.showerror("Erro", "Selecione um aluno.")
            return
        if not disciplina_selecionada:
            messagebox.showerror("Erro", "Selecione uma disciplina.")
            return
        if status not in ["Ativo", "Trancado", "Concluído"]:
            messagebox.showerror("Erro", "Status inválido.")
            return

        try:
            id_aluno = int(aluno_selecionado.split(" - ")[0])
        except Exception:
            messagebox.showerror("Erro", "Aluno inválido.")
            return

        try:
            id_disciplina = int(disciplina_selecionada.split(" - ")[0])
        except Exception:
            messagebox.showerror("Erro", "Disciplina inválida.")
            return

        if id_aluno not in df_alunos["ID"].values:
            messagebox.showerror("Erro", "Aluno não encontrado na base de dados.")
            return
        if id_disciplina not in df_disciplinas["ID"].values:
            messagebox.showerror("Erro", "Disciplina não encontrada na base de dados.")
            return

        data_matricula = datetime.now().strftime("%d/%m/%Y")

        nova_matricula = {
            "ID_Matricula": proximo_id,
            "ID_Aluno": id_aluno,
            "ID_Disciplina": id_disciplina,
            "Data_Matricula": data_matricula,
            "Status": status,
            "Observacao": observacao
        }

        df_matriculas = pd.concat([df_matriculas, pd.DataFrame([nova_matricula])], ignore_index=True)
        df_matriculas.to_csv(ARQUIVO_MATRICULAS, index=False, encoding='utf-8-sig')

        nome_aluno = df_alunos[df_alunos["ID"] == id_aluno]["Nome"].values[0]
        nome_disciplina = df_disciplinas[df_disciplinas["ID"] == id_disciplina]["Nome"].values[0]
        tree_matriculas.insert("", tk.END, values=(
            proximo_id, id_aluno, nome_aluno, id_disciplina, nome_disciplina,
            data_matricula, status, observacao
        ))

        messagebox.showinfo("Sucesso", f"Matrícula ID {proximo_id} salva com sucesso!")
        proximo_id += 1
        limpar_campos()

    def voltar():
        janela.destroy()
        from matriculas import tela_matricula
        tela_matricula.abrir_tela_matricula()

    # ========== 7. Botões ==========
    tk.Button(frame, text="Salvar Matrícula", font=("Times New Roman", 16, "bold"),
              fg="white", bg="darkgreen", activebackground="#5a9e50",
              relief="raised", bd=3, cursor="hand2",
              command=salvar_matricula).grid(row=5, column=0, columnspan=2, pady=15)

    tk.Button(frame, text="Limpar Campos", font=("Times New Roman", 14, "bold"),
              fg="white", bg="gray", activebackground="#888888",
              relief="raised", bd=3, cursor="hand2",
              command=limpar_campos).grid(row=6, column=0, columnspan=2, pady=5)

    tk.Button(frame, text="Voltar", font=("Times New Roman", 14, "bold"),
              fg="white", bg="#555555", activebackground="#333333",
              relief="raised", bd=3, cursor="hand2",
              command=voltar).grid(row=6, column=2, padx=20, pady=5)

    # ========== 8. Inicialização ==========
    atualizar_treeview()
    janela.mainloop()


if __name__ == "__main__":
    abrir_matricular_aluno()
