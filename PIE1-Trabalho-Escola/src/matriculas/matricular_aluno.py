import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
from datetime import datetime

ARQUIVO_MATRICULAS = "matriculas_totais.csv"

def abrir_matricular_aluno():

    # Carregar ou criar DataFrame de matrículas
    if os.path.exists(ARQUIVO_MATRICULAS):
        df = pd.read_csv(ARQUIVO_MATRICULAS)
    else:
        df = pd.DataFrame(columns=[
            "ID_Matricula",
            "ID_Aluno",
            "ID_Disciplina",
            "Data_Matricula",
            "Status",
            "Observacao"
        ])

    # Carregar alunos
    if os.path.exists("alunos_totais.csv"):
        alunos_df = pd.read_csv("alunos_totais.csv")
        lista_alunos = alunos_df["Nome"].tolist()
    else:
        lista_alunos = []

    # Carregar disciplinas
    if os.path.exists("disciplinas_totais.csv"):
        disciplinas_df = pd.read_csv("disciplinas_totais.csv")
        lista_disciplinas = disciplinas_df["Nome_Disciplina"].tolist()
    else:
        lista_disciplinas = []

    janela = tk.Tk()
    janela.title("Matricular Aluno - Sistema Escolar IF3000")
    janela.geometry("900x650")
    janela.configure(bg="lightgreen")

    tk.Label(
        janela,
        text="Nova Matrícula",
        font=("Times New Roman", 18, "bold"),
        fg="darkgreen",
        bg="lightgreen"
    ).grid(row=0, column=0, columnspan=2, pady=20)

    frame = tk.Frame(janela, bg="lightgreen")
    frame.grid(row=1, column=0, padx=20, pady=10, sticky="n")

    # Aluno
    tk.Label(
        frame,
        text="Aluno:",
        bg="lightgreen",
        font=("Arial", 12)
    ).grid(row=0, column=0, padx=5, pady=5)

    combo_aluno = ttk.Combobox(
        frame,
        values=lista_alunos,
        width=40
    )
    combo_aluno.grid(row=0, column=1, padx=5, pady=5)

    # Disciplina
    tk.Label(
        frame,
        text="Disciplina:",
        bg="lightgreen",
        font=("Arial", 12)
    ).grid(row=1, column=0, padx=5, pady=5)

    combo_disciplina = ttk.Combobox(
        frame,
        values=lista_disciplinas,
        width=40
    )
    combo_disciplina.grid(row=1, column=1, padx=5, pady=5)

    # Status
    tk.Label(
        frame,
        text="Status:",
        bg="lightgreen",
        font=("Arial", 12)
    ).grid(row=2, column=0, padx=5, pady=5)

    combo_status = ttk.Combobox(
        frame,
        values=["Ativo", "Trancado", "Concluído"],
        width=40
    )
    combo_status.grid(row=2, column=1, padx=5, pady=5)

    # Observação
    tk.Label(
        frame,
        text="Observação:",
        bg="lightgreen",
        font=("Arial", 12)
    ).grid(row=3, column=0, padx=5, pady=5)

    entry_obs = tk.Entry(frame, width=43)
    entry_obs.grid(row=3, column=1, padx=5, pady=5)

    # Treeview
    colunas = (
        "ID_Matricula",
        "ID_Aluno",
        "ID_Disciplina",
        "Data_Matricula",
        "Status"
    )

    tree = ttk.Treeview(
        janela,
        columns=colunas,
        show="headings",
        height=15
    )

    for coluna in colunas:
        tree.heading(coluna, text=coluna)
        tree.column(coluna, width=140)

    tree.grid(row=2, column=0, padx=20, pady=20)

    def atualizar_tree():
        for item in tree.get_children():
            tree.delete(item)

        for _, linha in df.iterrows():
            tree.insert(
                "",
                tk.END,
                values=(
                    linha["ID_Matricula"],
                    linha["ID_Aluno"],
                    linha["ID_Disciplina"],
                    linha["Data_Matricula"],
                    linha["Status"]
                )
            )
    def salvar_matricula():
        nonlocal df
        aluno = combo_aluno.get()
        disciplina = combo_disciplina.get()
        status = combo_status.get()
        observacao = entry_obs.get()
        if aluno == "":
            messagebox.showerror("Erro", "Selecione um aluno.")
            return
        if disciplina == "":
            messagebox.showerror("Erro", "Selecione uma disciplina.")
            return
        if status == "":
            messagebox.showerror("Erro", "Selecione um status.")
            return
        if len(df) == 0:
            proximo_id = 1
        else:
            proximo_id = int(df["ID_Matricula"].max()) + 1
        data_matricula = datetime.now().strftime("%d/%m/%Y")
        nova_matricula = {
            "ID_Matricula": proximo_id,
            "ID_Aluno": aluno,
            "ID_Disciplina": disciplina,
            "Data_Matricula": data_matricula,
            "Status": status,
            "Observacao": observacao
        }

        df.loc[len(df)] = nova_matricula
        df.to_csv(
            ARQUIVO_MATRICULAS,
            index=False
        )
        atualizar_tree()
        combo_aluno.set("")
        combo_disciplina.set("")
        combo_status.set("")
        entry_obs.delete(0, tk.END)

        messagebox.showinfo(
            "Sucesso",
            "Matrícula realizada com sucesso!"
        )
    def voltar():
        janela.destroy()
    botao_salvar = tk.Button(
        frame,
        text="Salvar Matrícula",
        command=salvar_matricula,
        width=20
    )
    botao_salvar.grid(row=4, column=0, pady=20)
    botao_voltar = tk.Button(
        frame,
        text="Voltar",
        command=voltar,
        width=20
    )
    botao_voltar.grid(row=4, column=1, pady=20)
    atualizar_tree()
    janela.mainloop()

if __name__ == "__main__":
    abrir_matricular_aluno()
