import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

ARQUIVO_ALUNOS = "alunos_totais.csv"

def tela_alterar_excluir():
    # Carregar dados
    if os.path.exists(ARQUIVO_ALUNOS):
        df = pd.read_csv(ARQUIVO_ALUNOS)
    else:
        df = pd.DataFrame(columns=["ID", "Nome", "Idade", "CPF", "Telefone", "Email"])

    janela = tk.Tk()
    janela.title("Alterar / Excluir Aluno")
    janela.geometry("900x650")
    janela.configure(bg="lightgreen")

    # Treeview
    colunas = ("ID", "Nome", "Idade", "CPF", "Telefone", "Email")
    tree = ttk.Treeview(janela, columns=colunas, show="headings", height=8)
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")
    tree.pack(pady=10)

    # Frame para os campos de edição
    frame_edicao = tk.Frame(janela, bg="lightgreen")
    frame_edicao.pack(pady=10)

    # ========== CAMPOS DE EDIÇÃO ==========
    label_nome = tk.Label(frame_edicao, text="Nome Completo:", font=("Times New Roman", 14), bg="lightgreen")
    label_nome.grid(row=0, column=0, sticky="e", padx=10, pady=5)
    entry_nome = tk.Entry(frame_edicao, font=("Times New Roman", 14), width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    label_idade = tk.Label(frame_edicao, text="Idade:", font=("Times New Roman", 14), bg="lightgreen")
    label_idade.grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entry_idade = tk.Entry(frame_edicao, font=("Times New Roman", 14), width=30)
    entry_idade.grid(row=1, column=1, padx=10, pady=5)

    label_cpf = tk.Label(frame_edicao, text="CPF:", font=("Times New Roman", 14), bg="lightgreen")
    label_cpf.grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entry_cpf = tk.Entry(frame_edicao, font=("Times New Roman", 14), width=30)
    entry_cpf.grid(row=2, column=1, padx=10, pady=5)

    label_telefone = tk.Label(frame_edicao, text="Telefone:", font=("Times New Roman", 14), bg="lightgreen")
    label_telefone.grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entry_telefone = tk.Entry(frame_edicao, font=("Times New Roman", 14), width=30)
    entry_telefone.grid(row=3, column=1, padx=10, pady=5)

    label_email = tk.Label(frame_edicao, text="Email:", font=("Times New Roman", 14), bg="lightgreen")
    label_email.grid(row=4, column=0, sticky="e", padx=10, pady=5)
    entry_email = tk.Entry(frame_edicao, font=("Times New Roman", 14), width=30)
    entry_email.grid(row=4, column=1, padx=10, pady=5)

    selected_id = tk.IntVar()

    def popular_treeview():
        for item in tree.get_children():
            tree.delete(item)
        for _, row in df.iterrows():
            tree.insert("", tk.END, values=(
                row["ID"], row["Nome"], row["Idade"],
                row["CPF"], row["Telefone"], row["Email"]
            ))

    def ao_selecionar(event):
        selecionado = tree.selection()
        if selecionado:
            valores = tree.item(selecionado[0])['values']
            selected_id.set(valores[0])
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, valores[1])
            entry_idade.delete(0, tk.END)
            entry_idade.insert(0, valores[2])
            entry_cpf.delete(0, tk.END)
            entry_cpf.insert(0, valores[3])
            entry_telefone.delete(0, tk.END)
            entry_telefone.insert(0, valores[4])
            entry_email.delete(0, tk.END)
            entry_email.insert(0, valores[5])

    tree.bind("<<TreeviewSelect>>", ao_selecionar)

    def limpar_campos():
        """Limpa os campos de edição e reseta o ID selecionado (usado internamente após alterar/excluir)"""
        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        selected_id.set(0)
        # Opcional: desmarca a seleção na treeview
        for item in tree.selection():
            tree.selection_remove(item)

    def alterar_aluno():
        nonlocal df
        if selected_id.get() == 0:
            messagebox.showerror("Erro", "Selecione um aluno primeiro.")
            return

        nome = entry_nome.get().strip()
        idade = entry_idade.get().strip()
        cpf = entry_cpf.get().strip()
        telefone = entry_telefone.get().strip()
        email = entry_email.get().strip()

        if not all([nome, idade, cpf, telefone, email]):
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return
        if not idade.isdigit():
            messagebox.showerror("Erro", "Idade deve ser um número inteiro.")
            return
        idade_int = int(idade)

        # Encontrar o índice do aluno
        idx = df[df["ID"] == selected_id.get()].index
        if len(idx) == 0:
            messagebox.showerror("Erro", "Aluno não encontrado.")
            return
        idx = idx[0]

        # Atualizar o DataFrame
        df.at[idx, "Nome"] = nome
        df.at[idx, "Idade"] = idade_int
        df.at[idx, "CPF"] = cpf
        df.at[idx, "Telefone"] = telefone
        df.at[idx, "Email"] = email

        df.to_csv(ARQUIVO_ALUNOS, index=False, encoding='utf-8-sig')
        popular_treeview()
        limpar_campos()
        messagebox.showinfo("Sucesso", f"Aluno ID {selected_id.get()} alterado com sucesso!")

    def excluir_aluno():
        nonlocal df
        if selected_id.get() == 0:
            messagebox.showerror("Erro", "Selecione um aluno.")
            return
        if messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir este aluno?"):
            df = df[df["ID"] != selected_id.get()]
            df.to_csv(ARQUIVO_ALUNOS, index=False, encoding='utf-8-sig')
            popular_treeview()
            limpar_campos()
            messagebox.showinfo("Sucesso", "Aluno excluído com sucesso!")

    def voltar_tela_aluno():
        janela.destroy()
        from alunos import tela_aluno
        tela_aluno.abrir_tela_aluno()
       

    # Botões
    frame_botoes = tk.Frame(janela, bg="lightgreen")
    frame_botoes.pack(pady=10)

    botao_alterar = tk.Button(frame_botoes, text="Alterar", font=("Times New Roman", 14),
                              bg="darkgreen", fg="white", command=alterar_aluno)
    botao_alterar.pack(side=tk.LEFT, padx=20)

    botao_excluir = tk.Button(frame_botoes, text="Excluir", font=("Times New Roman", 14),
                              bg="darkred", fg="white", command=excluir_aluno)
    botao_excluir.pack(side=tk.LEFT, padx=20)

    botao_voltar = tk.Button(frame_botoes, text="Voltar", font=("Times New Roman", 14),
                             bg="darkgreen", fg="white", command=voltar_tela_aluno)
    botao_voltar.pack(side=tk.RIGHT, padx=20)

    popular_treeview()
    janela.mainloop()

if __name__ == "__main__":
    tela_alterar_excluir()