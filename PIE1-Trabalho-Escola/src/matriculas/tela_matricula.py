import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

def abrir_tela_matricula():
    """Tela principal de gerenciamento de matrículas"""
    janela = tk.Tk()
    janela.title("Sistema Escolar IF3000 - Matrículas")
    janela.geometry("900x650")
    janela.configure(bg="lightgreen")

    label = tk.Label(janela, text="Tela de Matrículas",
                     font=("Times New Roman", 18, "bold"),
                     fg="darkgreen", bg="lightgreen")
    label.pack(pady=20)

    # ========== Funções de navegação ==========
    def matricular_aluno():
        janela.destroy()
        from matriculas import matricular_aluno as mat
        mat.abrir_matricular_aluno()

    def consultar_matriculas():
        janela.destroy()
        from matriculas import consultar_matricula
        consultar_matricula.abrir_consulta_matricula()

    def alterar_excluir_matricula():
        janela.destroy()
        from matriculas import alterar_excluir_m
        alterar_excluir_m.abrir_alterar_excluir()

    # Botões
    botao_matricular = tk.Button(janela, text="Matricular Aluno",
                                 font=("Times New Roman", 16, "bold"),
                                 fg="white", bg="darkgreen",
                                 command=matricular_aluno)
    botao_matricular.pack(pady=40)

    botao_consultar = tk.Button(janela, text="Consultar Matrículas",
                                font=("Times New Roman", 16, "bold"),
                                fg="white", bg="darkgreen",
                                command=consultar_matriculas)
    botao_consultar.pack(pady=40)

    botao_alterar = tk.Button(janela, text="Alterar/Excluir Matrícula",
                              font=("Times New Roman", 16, "bold"),
                              fg="white", bg="darkgreen",
                              command=alterar_excluir_matricula)
    botao_alterar.pack(pady=40)

    # Botão voltar (para menu principal, se desejar)
    def voltar_menu():
        janela.destroy()
        import telaPrincipal
        telaPrincipal.abrir_tela_principal()

    botao_voltar = tk.Button(janela, text="Voltar ao Menu",
                             font=("Times New Roman", 14, "bold"),
                             fg="white", bg="darkgreen",
                             command=voltar_menu)
    botao_voltar.pack(pady=20)

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela_matricula()

#class Matricula():
    #def __init__(self, id_matricula, id_aluno, id_disciplina, data_matricula, status, observacao):
        #self.id_matricula = id_matricula
        #self.id_aluno = id_aluno
        #self.id_disciplina = id_disciplina
        #self.data_matricula = data_matricula
        #self.status = status
        #self.observacao = observacao
