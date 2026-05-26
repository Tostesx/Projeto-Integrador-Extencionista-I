import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

ARQUIVO_DISCIPLINAS = "disciplinas_totais.csv"

def cadastrar_disciplina():
    # ========== Carregar Dados Existentes ==========
    if os.path.exists(ARQUIVO_DISCIPLINAS):
        df = pd.read_csv(ARQUIVO_DISCIPLINAS)
        # Verificar se o CSV não está vazio ou com colunas erradas
        if df.empty or not all(col in df.columns for col in ["ID", "Nome", "CargaHoraria", "Professor", "Curso"]):
            df = pd.DataFrame(columns=["ID", "Nome", "CargaHoraria", "Professor", "Curso"])
    else:
        df = pd.DataFrame(columns=["ID", "Nome", "CargaHoraria", "Professor", "Curso"])

    # Calcular próximo ID
    if not df.empty:
        proximo_id = df["ID"].max() + 1
    else:
        proximo_id = 1

    # ========== Interface Gráfica ==========
    janela = tk.Tk()
    janela.title("Cadastrar Disciplina - Sistema Escolar IF3000")
    janela.geometry("900x650")
    janela.configure(bg="lightgreen")

    label_titulo = tk.Label(janela, text="Cadastro de Disciplina", font=("Times New Roman", 18, "bold"),
                            fg="darkgreen", bg="lightgreen")
    label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

    frame = tk.Frame(janela, bg="lightgreen")
    frame.grid(row=1, column=0, padx=20, pady=10, sticky="n")

    # Campos de entrada
    label_nome = tk.Label(frame, text="Nome da Disciplina:", font=("Times New Roman", 14), bg="lightgreen")
    label_nome.grid(row=0, column=0, sticky="e", padx=10, pady=5)
    entry_nome = tk.Entry(frame, font=("Times New Roman", 14), width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    label_carga = tk.Label(frame, text="Carga Horária (h):", font=("Times New Roman", 14), bg="lightgreen")
    label_carga.grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entry_carga = tk.Entry(frame, font=("Times New Roman", 14), width=30)
    entry_carga.grid(row=1, column=1, padx=10, pady=5)

    label_professor = tk.Label(frame, text="Professor:", font=("Times New Roman", 14), bg="lightgreen")
    label_professor.grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entry_professor = tk.Entry(frame, font=("Times New Roman", 14), width=30)
    entry_professor.grid(row=2, column=1, padx=10, pady=5)

    label_curso = tk.Label(frame, text="Curso:", font=("Times New Roman", 14), bg="lightgreen")
    label_curso.grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entry_curso = tk.Entry(frame, font=("Times New Roman", 14), width=30)
    entry_curso.grid(row=3, column=1, padx=10, pady=5)

    # Treeview
    colunas = ("ID", "Nome", "CargaHoraria", "Professor", "Curso")
    tree_disciplinas = ttk.Treeview(janela, columns=colunas, show="headings", height=8)
    for col in colunas:
        tree_disciplinas.heading(col, text=col)
        tree_disciplinas.column(col, width=140, anchor="center")
    tree_disciplinas.grid(row=2, column=0, pady=20, padx=20, sticky="ew")

    # ========== Funções/Métodos ==========
    def atualizar_treeview():
        """Atualiza a Treeview com os dados do CSV atual"""
        for item in tree_disciplinas.get_children():
            tree_disciplinas.delete(item)
        if os.path.exists(ARQUIVO_DISCIPLINAS):
            df_temp = pd.read_csv(ARQUIVO_DISCIPLINAS)
            for _, row in df_temp.iterrows():
                tree_disciplinas.insert("", tk.END, values=(
                    row["ID"], row["Nome"], row["CargaHoraria"],
                    row["Professor"], row["Curso"]
                ))

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_carga.delete(0, tk.END)
        entry_professor.delete(0, tk.END)
        entry_curso.delete(0, tk.END)

    def adicionar_disciplina():
        nonlocal df, proximo_id

        nome = entry_nome.get().strip()
        carga = entry_carga.get().strip()
        professor = entry_professor.get().strip()
        curso = entry_curso.get().strip()

        if not all([nome, carga, professor, curso]):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        if not carga.isdigit():
            messagebox.showerror("Erro", "Carga horária deve ser um número inteiro.")
            return
        carga_int = int(carga)

        # Criar novo registro
        nova_disciplina = {
            "ID": proximo_id,
            "Nome": nome,
            "CargaHoraria": carga_int,
            "Professor": professor,
            "Curso": curso
        }

        # Adicionar ao DataFrame
        df = pd.concat([df, pd.DataFrame([nova_disciplina])], ignore_index=True)

        # Salvar no CSV
        df.to_csv(ARQUIVO_DISCIPLINAS, index=False, encoding='utf-8-sig')

        # Atualizar Treeview
        tree_disciplinas.insert("", tk.END, values=(proximo_id, nome, carga_int, professor, curso))

        messagebox.showinfo("Sucesso", f"Disciplina {nome} (ID {proximo_id}) cadastrada e salva!")
        proximo_id += 1
        limpar_campos()

    def voltar_tela_disciplina():
        janela.destroy()
        from disciplinas import tela_disciplina  # ajuste conforme sua estrutura
        tela_disciplina.abrir_tela_disciplina()

    # ========== Popular Treeview e Botões ==========
    atualizar_treeview()

    botao_salvar = tk.Button(frame, text="Salvar Disciplina", font=("Times New Roman", 16),
                             fg="white", bg="darkgreen", command=adicionar_disciplina)
    botao_salvar.grid(row=4, column=0, columnspan=2, pady=10)

    botao_voltar = tk.Button(frame, text="Voltar", font=("Times New Roman", 14),
                             fg="white", bg="darkgreen", command=voltar_tela_disciplina)
    botao_voltar.grid(row=4, column=2, padx=20, pady=5)

    janela.mainloop()

if __name__ == "__main__":
    cadastrar_disciplina()