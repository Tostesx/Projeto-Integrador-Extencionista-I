import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
from datetime import datetime

# Arquivo CSV que armazenará as matrículas
ARQUIVO_MATRICULAS = "matriculas_totais.csv"

def abrir_matricular_aluno():
    """Tela para realizar uma nova matrícula"""
    # DICA: Carregue o CSV de matrículas (se existir) em um DataFrame df.
    #       Caso não exista, crie um DataFrame vazio com as colunas:
    #       ["ID_Matricula", "ID_Aluno", "ID_Disciplina", "Data_Matricula", "Status", "Observacao"]
    
    # DICA: Calcule o próximo ID_Matricula (maior ID + 1 ou 1 se vazio)
    
    # ========== Interface ==========
    janela = tk.Tk()
    janela.title("Matricular Aluno - Sistema Escolar IF3000")
    janela.geometry("900x650")
    janela.configure(bg="lightgreen")
    
    # Título
    tk.Label(janela, text="Nova Matrícula", font=("Times New Roman", 18, "bold"),
             fg="darkgreen", bg="lightgreen").grid(row=0, column=0, columnspan=2, pady=20)
    
    frame = tk.Frame(janela, bg="lightgreen")
    frame.grid(row=1, column=0, padx=20, pady=10, sticky="n")
    
    # ========== Campos do formulário ==========
    # DICA: Use Combobox para selecionar aluno (carregue de alunos_totais.csv)
    #       e Combobox para disciplina (carregue de disciplinas_totais.csv)
    #       Campos: ID_Aluno, ID_Disciplina, Status (Ativo/Trancado/Concluído),
    #       Observacao (opcional). A data_matricula deve ser preenchida automaticamente
    #       com datetime.now().strftime("%d/%m/%Y")
    
    # Exemplo de Combobox:
    # label_aluno = tk.Label(frame, text="Aluno:", font=(...))
    # label_aluno.grid(...)
    # combo_aluno = ttk.Combobox(frame, values=lista_alunos, width=50)
    # combo_aluno.grid(...)
    
    # DICA: Use Treeview para mostrar as matrículas já cadastradas (opcional)
    
    # ========== Funções ==========
    def salvar_matricula():
        # Coletar dados dos campos
        # Validar se os campos obrigatórios estão preenchidos
        # Gerar novo ID
        # Criar dicionário com os dados
        # Adicionar ao DataFrame e salvar CSV
        # Atualizar Treeview e limpar campos
        # Exibir mensagem de sucesso
        pass
    
    def voltar():
        janela.destroy()
        from matricula import tela_matricula
        tela_matricula.abrir_tela_matricula()
    
    # Botões
    # botao_salvar = tk.Button(frame, text="Salvar Matrícula", command=salvar_matricula)
    # botao_voltar = tk.Button(frame, text="Voltar", command=voltar)
    
    # Popular Treeview (se houver)
    # janela.mainloop()

if __name__ == "__main__":
    abrir_matricular_aluno()