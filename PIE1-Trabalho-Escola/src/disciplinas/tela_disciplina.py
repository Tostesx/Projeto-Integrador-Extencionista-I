import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime

def abrir_tela_disciplina():
    janela = tk.Tk()
    janela.title("Sistema Escolar IF3000")
    janela.geometry("900x650")
    janela.configure(bg="lightgreen")

    label = tk.Label(janela, text="Tela de Disciplinas",
    font=("New Times Roman", 18, "bold"), fg="darkgreen", bg="lightgreen")
    label.pack(pady=20)

    def cadastrar_disciplina():
        janela.destroy()
        from disciplinas import cadastra_disciplina
        cadastra_disciplina.cadastrar_disciplina()

    botao_cadastra_disciplina = tk.Button(janela, text="Cadastrar Disciplina",
    font=("New Times Roman", 16, "bold"), fg="white", bg="darkgreen", command=cadastrar_disciplina)
    botao_cadastra_disciplina.pack(pady=40)

    def abrir_consulta_disciplina():
        janela.destroy()
        from disciplinas import consulta_disciplina
        consulta_disciplina.abrir_consulta_disciplina()

    botao_consulta_disciplina = tk.Button(janela, text="Lista de Disciplinas",
    font=("New Times Roman", 16, "bold"), fg="white", bg="darkgreen", command=abrir_consulta_disciplina)
    botao_consulta_disciplina.pack(pady=40)

    def abrir_alterar_excluir():
        janela.destroy()
        from disciplinas import alterar_excluir_d
        alterar_excluir_d.tela_alterar_excluir()

    botao_exclui_aluno = tk.Button(janela, text="Alterar/Excluir Disciplina", 
    font=("New Times Roman", 16, "bold"), fg="white", bg="darkgreen", command=abrir_alterar_excluir)
    botao_exclui_aluno.pack(pady=40)

    def voltar_menu_principal():
        janela.destroy()
        import telaPrincipal
        telaPrincipal.abrir_tela_principal()

    botao_menu_principal = tk.Button(janela, text="Voltar ao Menu Principal",
    font=("New Times Roman", 16, "bold"), fg="white", bg="darkgreen", command=voltar_menu_principal)
    botao_menu_principal.pack(pady=40)

    janela.mainloop()
if __name__ == "__main__":    
    abrir_tela_disciplina()

# A classe Disciplina foi comentada porque não é necessária para a funcionalidade atual da tela de disciplinas.
# Ela serva apenas como um modelo de dados para representar as informações de uma disciplina, mas não é utilizada diretamente na interface gráfica ou nas operações de cadastro, consulta, alteração ou exclusão de disciplinas. Se for necessário implementar funcionalidades adicionais que envolvam a manipulação de objetos Disciplina, a classe pode ser descomentada e utilizada conforme necessário.
#class Disciplina():
    #def __init__(self, id_disciplina, nome_disciplina, carga_horaria, professor, periodo):
        #self.id_disciplina = id_disciplina
        #self.nome_disciplina = nome_disciplina
        #self.carga_horaria = carga_horaria
        #self.professor = professor
        #self.periodo = periodo

