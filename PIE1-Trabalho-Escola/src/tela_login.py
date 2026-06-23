import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

ARQUIVO_USUARIOS = "usuarios.csv"

def abrir_tela_login():
    janela = tk.Tk()
    janela.title("Sistema Escolar IF3000 - Login")
    janela.geometry("500x400")
    janela.configure(bg="lightgreen")
    janela.resizable(False, False)

    # Centralizar
    janela.update_idletasks()
    largura, altura = 500, 400
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

    # Cabeçalho
    tk.Label(
        janela,
        text="Sistema Escolar IF3000",
        font=("Times New Roman", 22, "bold"),
        fg="darkgreen",
        bg="lightgreen"
    ).pack(pady=(40, 10))

    tk.Label(
        janela,
        text="Faça login para continuar",
        font=("Times New Roman", 14),
        fg="#2c3e50",
        bg="lightgreen"
    ).pack(pady=(0, 30))

    frame = tk.Frame(janela, bg="lightgreen")
    frame.pack(pady=10)

    tk.Label(
        frame,
        text="Login:",
        font=("Times New Roman", 14, "bold"),
        bg="lightgreen",
        fg="darkgreen"
    ).grid(row=0, column=0, sticky="e", padx=10, pady=10)

    entry_login = tk.Entry(
        frame,
        font=("Times New Roman", 14),
        width=25,
        relief="solid",
        bd=2
    )
    entry_login.grid(row=0, column=1, padx=10, pady=10)
    entry_login.focus()

    tk.Label(
        frame,
        text="Senha:",
        font=("Times New Roman", 14, "bold"),
        bg="lightgreen",
        fg="darkgreen"
    ).grid(row=1, column=0, sticky="e", padx=10, pady=10)

    entry_senha = tk.Entry(
        frame,
        font=("Times New Roman", 14),
        width=25,
        show="*",
        relief="solid",
        bd=2
    )
    entry_senha.grid(row=1, column=1, padx=10, pady=10)

    # ---------- Função de login melhorada ----------
    def fazer_login():
        login = entry_login.get().strip()
        senha = entry_senha.get().strip()

        if not login or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        # Verifica se o arquivo existe
        if not os.path.exists(ARQUIVO_USUARIOS):
            messagebox.showerror("Erro", "Arquivo de usuários não encontrado.")
            return

        try:
            # Lê o CSV com tratamento de espaços
            df = pd.read_csv(
                ARQUIVO_USUARIOS,
                encoding='utf-8',
                sep=',',
                skipinitialspace=True,
                dtype=str  # Lê tudo como string para evitar conversões
            )
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler arquivo: {e}")
            return

        # Verifica colunas
        colunas_necessarias = ["Login", "Senha"]
        if not all(col in df.columns for col in colunas_necessarias):
            messagebox.showerror("Erro", "Arquivo de usuários inválido (colunas: Login, Senha).")
            return

        # Remove espaços extras de todas as células (trata valores nulos)
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

        # Filtra usuário
        usuario = df[(df["Login"] == login) & (df["Senha"] == senha)]

        if not usuario.empty:
            messagebox.showinfo("Sucesso", f"Bem-vindo, {login}!")
            janela.destroy()
            from telaPrincipal import abrir_tela_principal
            abrir_tela_principal()
        else:
            messagebox.showerror("Erro", "Login ou senha inválidos.")

    def sair():
        if messagebox.askyesno("Sair", "Deseja realmente sair do sistema?"):
            janela.destroy()

    # Botões
    btn_entrar = tk.Button(
        janela,
        text="Entrar",
        font=("Times New Roman", 14, "bold"),
        fg="white",
        bg="darkgreen",
        activebackground="#5a9e50",
        activeforeground="white",
        relief="raised",
        bd=3,
        cursor="hand2",
        width=15,
        command=fazer_login
    )
    btn_entrar.pack(pady=15)

    btn_sair = tk.Button(
        janela,
        text="Sair",
        font=("Times New Roman", 14, "bold"),
        fg="white",
        bg="#8b0000",
        activebackground="#cc0000",
        activeforeground="white",
        relief="raised",
        bd=3,
        cursor="hand2",
        width=15,
        command=sair
    )
    btn_sair.pack(pady=5)

    # Atalhos
    janela.bind("<Return>", lambda event: fazer_login())
    janela.bind("<Escape>", lambda event: sair())

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela_login()