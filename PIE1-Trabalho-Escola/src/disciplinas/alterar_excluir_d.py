import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

# DICA: Altere o nome do arquivo CSV para o de disciplinas
ARQUIVO_DISCIPLINAS = "disciplinas_totais.csv"  # <-- COMPLETAR

def tela_alterar_excluir_disciplina():
    # ========== 1. Carregar dados ==========
    # DICA: Carregue o CSV de disciplinas para um DataFrame df.
    #       Se o arquivo não existir ou estiver vazio, crie um DataFrame
    #       com as colunas: ["ID", "Nome", "CargaHoraria", "Professor", "Curso"]
    # COMPLETAR AQUI:
    if os.path.exists(ARQUIVO_DISCIPLINAS):
        df = pd.read_csv(ARQUIVO_DISCIPLINAS)
        # Verificar colunas
        if df.empty or not all(col in df.columns for col in ["ID", "Nome", "CargaHoraria", "Professor", "Curso"]):
            df = pd.DataFrame(columns=["ID", "Nome", "CargaHoraria", "Professor", "Curso"])
    else:
        df = pd.DataFrame(columns=["ID", "Nome", "CargaHoraria", "Professor", "Curso"])

    # ========== 2. Interface gráfica ==========
    janela = tk.Tk()
    janela.title("Alterar / Excluir Disciplina - Sistema Escolar IF3000")  # Título adequado
    janela.geometry("900x650")
    janela.configure(bg="lightgreen")

    # Treeview para listar disciplinas
    colunas = ("ID", "Nome", "Carga Horária", "Professor", "Curso")
    tree = ttk.Treeview(janela, columns=colunas, show="headings", height=8)
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")
    tree.pack(pady=10)

    # Frame para os campos de edição
    frame_edicao = tk.Frame(janela, bg="lightgreen")
    frame_edicao.pack(pady=10)

    # ========== 3. Campos de edição (adaptados para disciplina) ==========
    # DICA: Crie labels e entries para:
    #       - Nome da disciplina
    #       - Carga horária (somente números)
    #       - Professor
    #       - Curso
    # Use grid para organizar (exatamente como no aluno)
    label_nome = tk.Label(frame_edicao, text="Nome da Disciplina:", font=("Times New Roman", 14), bg="lightgreen")
    label_nome.grid(row=0, column=0, sticky="e", padx=10, pady=5)
    entry_nome = tk.Entry(frame_edicao, font=("Times New Roman", 14), width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    label_carga = tk.Label(frame_edicao, text="Carga Horária (h):", font=("Times New Roman", 14), bg="lightgreen")
    label_carga.grid(row=1, column=0, sticky="e", padx=10, pady=5)
    entry_carga = tk.Entry(frame_edicao, font=("Times New Roman", 14), width=30)
    entry_carga.grid(row=1, column=1, padx=10, pady=5)

    label_professor = tk.Label(frame_edicao, text="Professor:", font=("Times New Roman", 14), bg="lightgreen")
    label_professor.grid(row=2, column=0, sticky="e", padx=10, pady=5)
    entry_professor = tk.Entry(frame_edicao, font=("Times New Roman", 14), width=30)
    entry_professor.grid(row=2, column=1, padx=10, pady=5)

    label_curso = tk.Label(frame_edicao, text="Curso:", font=("Times New Roman", 14), bg="lightgreen")
    label_curso.grid(row=3, column=0, sticky="e", padx=10, pady=5)
    entry_curso = tk.Entry(frame_edicao, font=("Times New Roman", 14), width=30)
    entry_curso.grid(row=3, column=1, padx=10, pady=5)

    # Variável para guardar o ID da disciplina selecionada
    selected_id = tk.IntVar()

    # ========== 4. Funções ==========
    def popular_treeview():
        """Atualiza a Treeview com os dados do DataFrame df (disciplinas)"""
        # DICA: Limpe a tree e reinsira todas as linhas do DataFrame
        for item in tree.get_children():
            tree.delete(item)
        for _, row in df.iterrows():
            tree.insert("", tk.END, values=(
                row["ID"], row["Nome"], row["CargaHoraria"],
                row["Professor"], row["Curso"]
            ))

    def ao_selecionar(event):
        """Quando uma linha da tree for clicada, carrega os dados nos campos de edição"""
        selecionado = tree.selection()
        if selecionado:
            valores = tree.item(selecionado[0])['values']
            selected_id.set(valores[0])
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, valores[1])
            entry_carga.delete(0, tk.END)
            entry_carga.insert(0, valores[2])
            entry_professor.delete(0, tk.END)
            entry_professor.insert(0, valores[3])
            entry_curso.delete(0, tk.END)
            entry_curso.insert(0, valores[4])

    tree.bind("<<TreeviewSelect>>", ao_selecionar)

    def limpar_campos():
        """Limpa os campos de edição e reseta o ID selecionado"""
        entry_nome.delete(0, tk.END)
        entry_carga.delete(0, tk.END)
        entry_professor.delete(0, tk.END)
        entry_curso.delete(0, tk.END)
        selected_id.set(0)
        # Opcional: desmarcar seleção na tree
        for item in tree.selection():
            tree.selection_remove(item)

    def alterar_disciplina():
        # DICA: Use nonlocal df para modificar o DataFrame externo
        nonlocal df
        if selected_id.get() == 0:
            messagebox.showerror("Erro", "Selecione uma disciplina primeiro.")
            return

        # Coletar dados dos campos
        nome = entry_nome.get().strip()
        carga = entry_carga.get().strip()
        professor = entry_professor.get().strip()
        curso = entry_curso.get().strip()

        # Validação: todos os campos preenchidos
        if not all([nome, carga, professor, curso]):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        # Validação: carga horária deve ser número inteiro
        # DICA: Use .isdigit() ou tente converter para int
        if not carga.isdigit():
            messagebox.showerror("Erro", "Carga horária deve ser um número inteiro.")
            return
        carga_int = int(carga)

        # Encontrar o índice da disciplina no DataFrame
        idx = df[df["ID"] == selected_id.get()].index
        if len(idx) == 0:
            messagebox.showerror("Erro", "Disciplina não encontrada.")
            return
        idx = idx[0]

        # Atualizar o DataFrame
        df.at[idx, "Nome"] = nome
        df.at[idx, "CargaHoraria"] = carga_int
        df.at[idx, "Professor"] = professor
        df.at[idx, "Curso"] = curso

        # Salvar no CSV
        df.to_csv(ARQUIVO_DISCIPLINAS, index=False, encoding='utf-8-sig')
        popular_treeview()
        limpar_campos()
        messagebox.showinfo("Sucesso", f"Disciplina ID {selected_id.get()} alterada com sucesso!")

    def excluir_disciplina():
        nonlocal df
        if selected_id.get() == 0:
            messagebox.showerror("Erro", "Selecione uma disciplina.")
            return
        if messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir esta disciplina?"):
            # DICA: Filtre o DataFrame mantendo apenas registros com ID diferente do selecionado
            df = df[df["ID"] != selected_id.get()]
            df.to_csv(ARQUIVO_DISCIPLINAS, index=False, encoding='utf-8-sig')
            popular_treeview()
            limpar_campos()
            messagebox.showinfo("Sucesso", "Disciplina excluída com sucesso!")

    def voltar_tela_disciplina():
        janela.destroy()
        # DICA: Importe a tela principal de disciplinas (ex: from disciplinas import tela_disciplina)
        from disciplinas import tela_disciplina  # <-- COMPLETAR conforme sua estrutura
        tela_disciplina.abrir_tela_disciplina()

    # ========== 5. Botões ==========
    frame_botoes = tk.Frame(janela, bg="lightgreen")
    frame_botoes.pack(pady=10)

    botao_alterar = tk.Button(frame_botoes, text="Alterar", font=("Times New Roman", 14),
                              bg="darkgreen", fg="white", command=alterar_disciplina)
    botao_alterar.pack(side=tk.LEFT, padx=20)

    botao_excluir = tk.Button(frame_botoes, text="Excluir", font=("Times New Roman", 14),
                              bg="darkred", fg="white", command=excluir_disciplina)
    botao_excluir.pack(side=tk.LEFT, padx=20)

    # DICA: Adicione um botão "Limpar" se desejar (opcional) – pode ser útil
    # botao_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar_campos)
    # botao_limpar.pack(side=tk.LEFT, padx=20)

    botao_voltar = tk.Button(frame_botoes, text="Voltar", font=("Times New Roman", 14),
                             bg="darkgreen", fg="white", command=voltar_tela_disciplina)
    botao_voltar.pack(side=tk.RIGHT, padx=20)

    # ========== 6. Inicialização ==========
    popular_treeview()
    janela.mainloop()

if __name__ == "__main__":
    tela_alterar_excluir_disciplina()