import tkinter as tk

class Produto:
    def __init__(self, codigo, nome, preco, tipo, quantidadeEstoque):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
        self.quantidadeEstoque = quantidadeEstoque

def adicionarProduto():
    codigo = entradaCodigo.get()
    nome = entradaNome.get()
    preco = entradaPreco.get()
    tipo = entradaTipo.get()
    quantidadeEstoque = entradaQuantidade.get()
    produto = Produto(codigo, nome, preco, tipo, quantidadeEstoque)
    listaDeProdutos.append(produto)
    limparFormularioProduto()

def listarProdutos():
    print("Lista de Produtos: ")
    for produto in listaDeProdutos:
        print("Produto: ")
        print("Codigo: ", produto.codigo)
        print("Nome: ", produto.nome)
        print("Quantidade: ", produto.quantidadeEstoque)
        print("Tipo: ", produto.tipo)

def limparFormularioProduto():
    entradaCodigo.delete(0, tk.END)
    entradaNome.delete(0, tk.END)
    entradaTipo.delete(0, tk.END)
    entradaPreco.delete(0, tk.END)
    entradaQuantidade.delete(0, tk.END)

#Criar lista vazia
listaDeProdutos = []

#Criação e Configuração
janela = tk.Tk()
janela.title("Projeto Integrador extensionista 1")
janela.geometry("800x600")
#definir a cor e a transparência da jannela
janela.config(bg="lightblue")
janela.attributes("-alpha", 1)

labelTitulo = tk.Label(
    janela,
    text="Bem Vindo ao APP PIE1",
    font=("Comic Sans MT", 18, "bold"),
    bg="lightblue",
    fg="darkblue",
    pady=20,
    padx=80
)
labelTitulo.grid(row=0, column=1)

labelCadastro = tk.Label(
    janela,
    text="Cadastro de Produto: ",
    font=("Comic Sans MT", 12, "bold"),
    bg="lightblue",
    fg="darkblue",
    pady=10
)
labelCadastro.grid(row=1, column=0, padx=(35, 0), sticky="e")

labelProduto = tk.Label(
    janela,
    text="Produto: ",
    font=("Comic Sans MT", 12, "bold"),
    bg="lightblue",
    fg="darkblue",
    pady=10
)
labelProduto.grid(row=2, column=0, padx=(35, 0), sticky="e")

labelCodigo = tk.Label(
    janela,
    text="Código: ",
    font=("Comic Sans MT", 12, "bold"),
    bg="lightblue",
    fg="darkblue",
    pady=10
)
labelCodigo.grid(row=3, column=0, padx=(35, 0), sticky="e")
entradaCodigo = tk.Entry(janela)
entradaCodigo.grid(row=3, column=1, padx=(0, 40))

labelNome = tk.Label(
    janela,
    text="Nome: ",
    font=("Comic Sans MT", 12, "bold"),
    bg="lightblue",
    fg="darkblue",
    pady=10
)
labelNome.grid(row=4, column=0, padx=(35, 0), sticky="e")
entradaNome = tk.Entry(janela)
entradaNome.grid(row=4, column=1, padx=(0, 40))


labelPreco = tk.Label(
    janela,
    text="Preço: ",
    font=("Comic Sans MT", 12, "bold"),
    bg="lightblue",
    fg="darkblue",
    pady=10
)
labelPreco.grid(row=5, column=0, padx=(35, 0), sticky="e")
entradaPreco = tk.Entry(janela)
entradaPreco.grid(row=5, column=1, padx=(0, 40))



labelQuantidadeEmEstoque = tk.Label(
    janela,
    text="Quantidade em Estoque: ",
    font=("Comic Sans MT", 12, "bold"),
    bg="lightblue",
    fg="darkblue",
    pady=10
)
labelQuantidadeEmEstoque.grid(row=6, column=0, padx=(40, 0), sticky="e")
entradaQuantidade = tk.Entry(janela)
entradaQuantidade.grid(row=6, column=1, padx=(0, 40))


labelTipo = tk.Label(
    janela,
    text="Tipo: ",
    font=("Comic Sans MT", 12, "bold"),
    bg="lightblue",
    fg="darkblue",
    pady=10
)
labelTipo.grid(row=7, column=0, padx=(35, 0), sticky="e")
entradaTipo = tk.Entry(janela)
entradaTipo.grid(row=7, column=1, padx=(0, 40))

botaoListar = tk.Button(
    text="listar Produtos",
    font=("Comic Sans MT", 12, "bold"),
    bg="darkblue",
    fg="red",
    command=listarProdutos
)
botaoListar.grid(row=8, column=0, padx=(40,0), sticky="e")


botaoCadastro = tk.Button(
    text="Cadastrar Produto",
    font=("Comic Sans MT", 12, "bold"),
    bg="darkblue",
    fg="red",
    command=adicionarProduto
)
botaoCadastro.grid(row=8, column=1)

# Loop janela
janela.mainloop()