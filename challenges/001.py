livros = {}
usuarios = {}

# Função para adicionar livro

def adicionar_livro():
    id_livro = input("Qual o id do livro que deseja adicionar?")
    if id_livro in livros:
        print("Este livro já esta cadastrado.")

    else:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        livros[id_livro] = {
            "Titulo": titulo,
            "Autor": autor,
            "Disponivel": True,
            "Usuario": None
        }
        print("Livro adicionado com sucesso!!!")

# Função para adicionar usuario

def adicionar_usuario():
    id_usuario = input("Qual o id do usuario que deseja adicionar?")
    usuario_existe = id_usuario in usuarios
    if usuario_existe:
        print("Este usuario já esta cadastrado.")
    else:
        nome = input("Digite o nome do usuário: ")
        usuarios[id_usuario] = {
            "nome": nome,
            "livros_emprestados": []
        }
        print("Usuário adicionado com sucesso.")
        print(usuarios[id_usuario])

# Função para emprestar livro

def emprestar_livro():
    id_livro = input("Digite o ID do livro: ")
    id_usuario = input("Digite o ID do usuário: ")

    if id_livro not in livros:
        print("Livro não encontrado.")
    elif not livros[id_livro]["disponivel"]:
        print("Livro já foi emprestado.")
    elif id_usuario not in usuarios:
        print("Usuário não encontrado.")
    else:
        livros[id_livro]["disponivel"] = False
        livros[id_livro]["usuario"] = id_usuario
        usuarios[id_usuario]["livros_emprestados"].append(id_livro)
        print(f"Livro '{livros[id_livro]['titulo']}' emprestado com sucesso para {usuarios[id_usuario]['nome']}.")

# Função para devolver um livro

def devolver_livro():
    id_livro = input("Digite o ID do livro: ")

    if id_livro not in livros:
        print("Livro não encontrado.")
    elif livros[id_livro]["disponivel"]:
        print("Livro já está disponível.")
    else:
        id_usuario = livros[id_livro]["usuario"]
        livros[id_livro]["disponivel"] = True
        usuarios[id_usuario]["livros_emprestados"].remove(id_livro)
        livros[id_livro]["usuario"] = None
        print(f"Livro '{livros[id_livro]['titulo']}' devolvido com sucesso.")

# Função para mostrar o relatorio de um livro

def mostrar_relatorio_livro():
    id_livro = input("Digite o ID do livro: ")

    if id_livro in livros:
        livro = livros[id_livro]
        status = "Disponível" if livro["disponivel"] else f"Emprestado para {usuarios[livro['usuario']]['nome']}"
        print(f"ID: {id_livro}, Título: {livro['titulo']}, Autor: {livro['autor']}, Status: {status}")
    else:
        print("Livro não encontrado.")

# Função para mostrar o relatorio de todos os livros

def mostrar_relatorio_todos_livros():
    if livros:
        for id_livro, livro in livros.items():
            status = "Disponível" if livro["disponivel"] else f"Emprestado para {usuarios[livro['usuario']]['nome']}"
            print(f"ID: {id_livro}, Título: {livro['titulo']}, Autor: {livro['autor']}, Status: {status}")
    else:
        print("Nenhum livro cadastrado.")


# Função para mostrar o relatorio de um usuario
def mostrar_relatorio_usuario():
    id_usuario = input("Digite o ID do usuário: ")

    if id_usuario in usuarios:
        usuario = usuarios[id_usuario]
        print(f"Nome: {usuario['nome']}, Livros emprestados: {usuario['livros_emprestados']}")
    else:
        print("Usuário não encontrado.")

# Função para mostrar o relatorio de todos os usuarios

def mostrar_relatorio_todos_usuarios():
    if usuarios:
        for id_usuario, usuario in usuarios.items():
            print(f"ID: {id_usuario}, Nome: {usuario['nome']}, Livros emprestados: {usuario['livros_emprestados']}")
    else:
        print("Nenhum usuário cadastrado.")


#
#   Menu Principal em Loop
#


def menu_principal():
    while True:
        print("\nSistema de Gerenciamento de Biblioteca")
        print("1. Adicionar Novo Livro")
        print("2. Adicionar Novo Usuário")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Mostrar Relatório de um Livro")
        print("6. Mostrar Relatório de Todos os Livros")
        print("7. Mostrar Relatório de um Usuário")
        print("8. Mostrar Relatório de Todos os Usuários")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_livro()
        elif opcao == '2':
            adicionar_usuario()
        elif opcao == '3':
            emprestar_livro()
        elif opcao == '4':
            devolver_livro()
        elif opcao == '5':
            mostrar_relatorio_livro()
        elif opcao == '6':
            mostrar_relatorio_todos_livros()
        elif opcao == '7':
            mostrar_relatorio_usuario()
        elif opcao == '8':
            mostrar_relatorio_todos_usuarios()
        elif opcao == '9':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Ativa o MENU
menu_principal()