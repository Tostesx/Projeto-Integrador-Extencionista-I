import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

ARQUIVO_ALUNOS = "alunos_totais.csv"

def cadastrar_aluno():
    # ========== Carregar Dados Existentes ==========
    if os.path.exists(ARQUIVO_ALUNOS):
        df = pd.read_csv(ARQUIVO_ALUNOS)
        # Verificar se o CSV não está vazio ou com colunas erradas
        if df.empty or not all(col in df.columns for col in ["ID", "Nome", "Idade", "CPF", "Telefone", "Email"]):
            df = pd.DataFrame(columns=["ID", "Nome", "Idade", "CPF", "Telefone", "Email"])
    else:
        df = pd.DataFrame(columns=["ID", "Nome", "Idade", "CPF", "Telefone", "Email"])

    # Calcular próximo ID
    if not df.empty:
        proximo_id = df["ID"].max() + 1
    else:
        proximo_id = 1

    # ========== Interface Gráfica ==========
    janela = tk.Tk()
    janela.title("Cadastrar Aluno - Sistema Escolar IF3000")
    janela.geometry("900x650")
    janela.configure(bg="lightgreen")

    label_titulo = tk.Label(janela, text="Cadastro de Aluno", font=("Times New Roman", 18, "bold"),
                            fg="darkgreen", bg="lightgreen")
    label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

    frame = tk.Frame(janela, bg="lightgreen")
    frame.grid(row=1, column=0, padx=20, pady=10, sticky="n")

    # Campos de entrada
    label_nome = tk.Label(frame, text="Nome Completo:", font=("Times New Roman", 14), bg="lightgreen")
    label_nome.grid(row=0, column=0, sticky="e", padx=10, pady=5)
    entry_nome = tk.Entry(frame, font=("Times New Roman", 14), width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    label_idade = tk.Label(frame, text="Idade:", font=("Times New Roman", 14), bg="lightgreen")
    label_idade.grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entry_idade = tk.Entry(frame, font=("Times New Roman", 14), width=30)
    entry_idade.grid(row=1, column=1, padx=10, pady=5)

    label_cpf = tk.Label(frame, text="CPF:", font=("Times New Roman", 14), bg="lightgreen")
    label_cpf.grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entry_cpf = tk.Entry(frame, font=("Times New Roman", 14), width=30)
    entry_cpf.grid(row=2, column=1, padx=10, pady=5)

    label_telefone = tk.Label(frame, text="Telefone:", font=("Times New Roman", 14), bg="lightgreen")
    label_telefone.grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entry_telefone = tk.Entry(frame, font=("Times New Roman", 14), width=30)
    entry_telefone.grid(row=3, column=1, padx=10, pady=5)

    label_email = tk.Label(frame, text="Email:", font=("Times New Roman", 14), bg="lightgreen")
    label_email.grid(row=4, column=0, sticky="e", padx=10, pady=5)
    entry_email = tk.Entry(frame, font=("Times New Roman", 14), width=30)
    entry_email.grid(row=4, column=1, padx=10, pady=5)

    # Treeview
    colunas = ("ID", "Nome", "Idade", "CPF", "Telefone", "Email")
    tree_alunos = ttk.Treeview(janela, columns=colunas, show="headings", height=8)
    for col in colunas:
        tree_alunos.heading(col, text=col)
        tree_alunos.column(col, width=120, anchor="center")
    tree_alunos.grid(row=2, column=0, pady=20, padx=20, sticky="ew")

    # ========== Funções/Métodos ==========
    def atualizar_treeview():
        """Atualiza a Treeview com os dados do CSV atual"""
        for item in tree_alunos.get_children():
            tree_alunos.delete(item)
        if os.path.exists(ARQUIVO_ALUNOS):
            df_temp = pd.read_csv(ARQUIVO_ALUNOS)
            for _, row in df_temp.iterrows():
                tree_alunos.insert("", tk.END, values=(
                    row["ID"], row["Nome"], row["Idade"],
                    row["CPF"], row["Telefone"], row["Email"]
                ))

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_email.delete(0, tk.END)

    def adicionar_aluno():
        nonlocal df, proximo_id # Permite modificar as variáveis da função externa

        nome = entry_nome.get().strip()
        idade = entry_idade.get().strip()
        cpf = entry_cpf.get().strip()
        telefone = entry_telefone.get().strip()
        email = entry_email.get().strip()

        if not all([nome, idade, cpf, telefone, email]):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        if not idade.isdigit():
            messagebox.showerror("Erro", "Idade deve ser um número inteiro.")
            return
        idade_int = int(idade)

        # Criar novo registro
        novo_aluno = {
            "ID": proximo_id,
            "Nome": nome,
            "Idade": idade_int,
            "CPF": cpf,
            "Telefone": telefone,
            "Email": email
        }

        # Adicionar ao DataFrame (evita warning usando concat)
        df = pd.concat([df, pd.DataFrame([novo_aluno])], ignore_index=True)

        # Salvar no CSV
        df.to_csv(ARQUIVO_ALUNOS, index=False, encoding='utf-8-sig')

        # Atualizar Treeview
        tree_alunos.insert("", tk.END, values=(proximo_id, nome, idade_int, cpf, telefone, email))

        messagebox.showinfo("Sucesso", f"Aluno {nome} (ID {proximo_id}) cadastrado e salvo!")
        proximo_id += 1
        limpar_campos()

    def voltar_tela_aluno():
        janela.destroy()
        from alunos import tela_aluno
        tela_aluno.abrir_tela_aluno()  

    # ========== Popular Treeview e Botões ==========
    atualizar_treeview()  # <-- ESSENCIAL: carrega os dados existentes

    botao_salvar = tk.Button(frame, text="Salvar Aluno", font=("Times New Roman", 16),
                             fg="white", bg="darkgreen", command=adicionar_aluno)
    botao_salvar.grid(row=5, column=0, columnspan=2, pady=10)

    botao_voltar = tk.Button(frame, text="Voltar", font=("Times New Roman", 14),
                             fg="white", bg="darkgreen", command=voltar_tela_aluno)
    botao_voltar.grid(row=5, column=2, padx=20, pady=5)

    janela.mainloop()

if __name__ == "__main__":
    cadastrar_aluno()