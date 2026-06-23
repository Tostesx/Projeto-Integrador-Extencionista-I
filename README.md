🏫 Sistema Escolar IF3000

Projeto Integrador Extencionista I
Curso: Desenvolvimento de Software Multiplataforma (Fatec)

Autores:

    Lucas Victor

    Matheus Reis

    Matheus Tostes

    Taylor Vilela

📌 Sobre o Projeto

O Sistema Escolar IF3000 é uma aplicação desktop desenvolvida em Python com interface gráfica Tkinter, projetada para gerenciar alunos, disciplinas e matrículas de uma instituição de ensino. O sistema oferece uma experiência intuitiva, com telas organizadas em abas (Notebook), botões estilizados e um fluxo de autenticação seguro via login.
🎯 Funcionalidades
🔐 Autenticação

    Tela de login com validação de credenciais armazenadas em arquivo CSV.

    Usuários pré-cadastrados: login e senha fixos (administrador pode editar o CSV).

    Atalhos de teclado: Enter para login, Esc para sair.

👨‍🎓 Gerenciamento de Alunos

    Cadastrar aluno: formulário com campos: Nome, Idade, CPF, Telefone, E-mail.

    Listar alunos: tabela com todos os registros (scroll, atualização automática).

    Alterar/Excluir aluno: selecione um aluno na lista, edite os campos e salve ou exclua permanentemente.

📚 Gerenciamento de Disciplinas

    Cadastrar disciplina: Nome, Carga Horária (inteiro), Professor, Curso.

    Listar disciplinas: tabela com todos os registros.

    Alterar/Excluir disciplina: edição e remoção de disciplinas.

📋 Gerenciamento de Matrículas

    Matricular aluno: selecione aluno e disciplina (comboboxes carregados dinamicamente dos CSVs), status (Ativo/Trancado/Concluído) e observação opcional.

    Consultar matrículas: exibe todas as matrículas com nomes de alunos e disciplinas (merge automático).

    Alterar/Excluir matrícula: edite ou remova matrículas existentes.

🎨 Interface

    Tema visual unificado (verde claro lightgreen, verde escuro darkgreen).

    Botões padronizados com efeitos hover, fonte Times New Roman.

    Abas (Notebook) para navegação entre os módulos.

    Botão "Sair do Sistema" em destaque.

🧰 Tecnologias Utilizadas

    Python 3.14+ – linguagem principal.

    Tkinter / ttk – interface gráfica nativa.

    Pandas – manipulação e persistência de dados em CSV.

    CSV (arquivos locais) – armazenamento dos dados:

        alunos_totais.csv

        disciplinas_totais.csv

        matriculas_totais.csv

        usuarios.csv (login)

📁 Estrutura de Pastas
text

src/
├── telaPrincipal.py          # Tela principal com abas
├── tela_login.py             # Tela de login
├── alunos/
│   ├── tela_aluno.py         # Menu alunos
│   ├── cadastra_aluno.py     # Cadastro
│   ├── consulta_aluno.py     # Listagem
│   └── alterar_excluir.py    # Editar/remover
├── disciplinas/
│   ├── tela_disciplina.py    # Menu disciplinas
│   ├── cadastra_disciplina.py
│   ├── consulta_disciplina.py
│   └── alterar_excluir_d.py
├── matriculas/
│   ├── tela_matricula.py     # Menu matrículas
│   ├── matricular_aluno.py   # Nova matrícula
│   ├── consultar_matricula.py
│   └── alterar_excluir_m.py
└── usuários.csv              # Credenciais (fora do src, na raiz)

⚙️ Pré‑requisitos

    Python 3.14 ou superior.

    Bibliotecas Python:

        pandas

        tkinter (já inclusa no Python padrão)

        os (nativa)

Instale as dependências (se necessário):
bash

pip install pandas

🚀 Como Executar

    Clone o repositório:
    bash

    git clone https://github.com/seu-usuario/projeto-escolar.git
    cd projeto-escolar/src

    Certifique-se de que o arquivo usuarios.csv está na raiz do projeto (mesmo diretório de tela_login.py). Se não existir, você pode criá-lo manualmente com o conteúdo:
    csv

    ID,Login,Senha
    1,Lucas,123
    2,Tostes,123
    3,Taylor,123
    4,Reis,123

    Execute a tela de login:
    bash

    python tela_login.py

    Faça login com uma das credenciais acima e comece a usar o sistema.

🧩 Persistência dos Dados

Todos os dados são salvos automaticamente em arquivos CSV no mesmo diretório onde o programa é executado. Isso facilita a portabilidade e a edição manual, se necessário. Os arquivos são recriados com a estrutura correta caso estejam ausentes ou corrompidos.
🔧 Melhorias Futuras (Sugestões)

    Implementar criptografia para senhas.

    Adicionar filtros e ordenação nas listagens.

    Exportar relatórios para PDF/Excel.

    Suporte a múltiplos usuários com diferentes níveis de permissão.

    Criar um instalador para distribuição.

🤝 Contribuição

Este projeto foi desenvolvido como trabalho acadêmico. Sugestões e melhorias são bem‑vindas! Caso queira contribuir, siga os passos:

    Faça um fork do repositório.

    Crie uma branch para sua feature (git checkout -b minha-feature).

    Commit suas mudanças (git commit -m 'Adiciona minha feature').

    Push para a branch (git push origin minha-feature).

    Abra um Pull Request.

📄 Licença

Este projeto é de uso acadêmico e educativo, sem fins comerciais. Sinta‑se livre para utilizá‑lo como base para estudos.

Desenvolvido com ❤️ pela equipe IF3000 Primeiro Período Ciências da Computação.
