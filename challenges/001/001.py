import json
import os

json_file = "teste.json"

# Dicionários de exemplo para livros e usuários
livros = {}
usuarios = {}

# Função para carregar os dados do JSON
def carregar_dados():
    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            dados = json.load(f)
            livros.update(dados.get("livros", {}))
            usuarios.update(dados.get("usuarios", {}))
    else:
        print(f"{json_file} não existe, criando um novo...")

# Função para salvar os dados no JSON
def salvar_dados():
    with open(json_file, "w") as f:
        json.dump({"livros": livros, "usuarios": usuarios}, f, indent=2)

# Função para adicionar um valor novo ao dicionário e salvar no JSON
def adicionar_ao_dicionario(dicionario, chave, valor):
    dicionario[chave] = valor
    salvar_dados()

carregar_dados()



# Acessa uma estante de livros / biblioteca

def acessar_biblioteca():
    print("\n Uma estante com todos os livros da biblioteca!")
    for id_livro, livro in livros.items():
        print(f"> // {livro['titulo']} //")


# Função que adiciona um livro

def adicionar_livro():
    id_livro = input("Digite o ID do seu novo livro: ")
    if id_livro in livros:
        print(">>>>> ESTE LIVRO JÁ EXISTE<<<<<")
    else:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        livros[id_livro] = {
            "titulo": titulo,
            "autor": autor,
            "disponivel": True,
            "livro": id_livro
        }
        print("\n>>>>> LIVRO CADASTRADO COM SUCESSO <<<<<")
        print(f"> Titulo: {titulo}\n> Autor: {autor}")


# Função que adiciona um usuario

def adicionar_usuario():
    id_usuario = input("\nQual o id do usuário que deseja adicionar? ")
    if id_usuario in usuarios:
        print("\n>>>>> ESTE USUÁRIO JÁ ESTÁ CADASTRADO <<<<<")
    else:
        nome_usuario = input("Digite o nome do usuário: ")  # Renomeado para evitar confusão
        usuarios[id_usuario] = {
            "nome": nome_usuario,
            "id_usuario": id_usuario,
            "livros_emprestados": []
        }
        print("\n>>>>> USUÁRIO CADASTRADO COM SUCESSO <<<<<")
        print(f"\n> ID: {id_usuario}\n> Nome: {usuarios[id_usuario]['nome']}\n> Livros emprestados: {usuarios[id_usuario]['livros_emprestados']}")



# Função que empresta um livro

def emprestar_livro():
    print("\nQual livro você deseja emprestar? ")
    for id_livro, livro in livros.items():
        print(f"> ID: {id_livro} -- Título: {livro['titulo']}")
    id_livro = input("Digite o ID do que deseja: ")

    print("\nDigite o ID do usuário: ")
    if usuarios:
        for id_usuario, usuario in usuarios.items():
            print(
                f"> ID: {usuario['id_usuario']} -- Nome: {usuario['nome']}")
    id_usuario = input("Digite o ID do que deseja: ")

    if id_livro not in livros:
        print("\n>>>>> ESTE LIVRO NÃO ESTA CADASTRADO NO SISTEMA <<<<<")
    elif not livros[id_livro]["disponivel"]:
        print(">>>>> LIVRO JÁ FOI EMPRESTADO <<<<<")
    elif id_usuario not in usuarios:
        print("Usuário não encontrado.")
    else:
        livros[id_livro]["disponivel"] = False
        livros[id_livro]["usuario"] = id_usuario
        usuarios[id_usuario]["livros_emprestados"].append(id_livro)
        print(f">>>>> O livro '{livros[id_livro]['titulo']}' foi emprestado com sucesso para {usuarios[id_usuario]['nome']}. <<<<<")


# Função que devolve um livro

def devolver_livro():
    print("\nQual livro você deseja devolver? ")
    for id_livro, livro in livros.items():
        print(f"> ID: {id_livro} -- Título: {livro['titulo']}")
    id_livro = input("Digite o ID do que deseja: ")

    if id_livro not in livros:
        print(">>>>> LIVRO NÃO ENCONTRADO <<<<<")
    elif livros[id_livro]["disponivel"]:
        print("Livro já está disponível.")
    else:
        id_usuario = livros[id_livro]["usuario"]
        livros[id_livro]["disponivel"] = True
        usuarios[id_usuario]["livros_emprestados"].remove(id_livro)
        livros[id_livro]["usuario"] = None
        print(f"Livro '{livros[id_livro]['titulo']}' devolvido com sucesso.")


# Função para mostrar o relatório de um livro

def mostrar_relatorio_livro():
    print("\nQual dos livros abaixo você gostaria de receber um relatorio? ")
    for id_livro, livro in livros.items():
        print(f"> ID: {id_livro} -- Título: {livro['titulo']}")
    id_livro = input("Digite o ID do livro: ")


    if id_livro in livros:
        livro = livros[id_livro]
        status = "disponível" if livro["disponivel"] else f"Emprestado para {usuarios[livro['usuario']]['nome']}"
        print(f"\n> ID: {id_livro}\n> Título: {livro['titulo']}\n> Autor: {livro['autor']}\n> status: {status}")
    else:
        print(">>>>> LIVRO NÃO ENCONTRADO <<<<<")


# Função para mostrar o relatório de todos os livros

def mostrar_relatorio_todos_livros():
    if livros:
        for id_livro, livro in livros.items():
            status = "disponível" if livro[
                "disponivel"] else f"Emprestado para {usuarios[livro['usuario']]['nome']}"
            print(f"\n> ID: {id_livro}\n> Título: {livro['titulo']}\n> Autor: {livro['autor']}\n> Status: {status}")
    else:
        print(">>>>> NENHUM LIVRO CADASTRADO <<<<<")


# Função para mostrar o relatório de um usuario

def mostrar_relatorio_usuario():
    print("\nQual dos usuarios abaixo você gostaria de receber um relatorio? ")
    if usuarios:
        for id_usuario, usuario in usuarios.items():
            print(
                f"> ID: {usuario['id_usuario']} -- Nome: {usuario['nome']}")
    id_usuario = input("Digite o ID do que deseja: ")

    if id_usuario in usuarios:
        usuario = usuarios[id_usuario]
        print(f"\n> Nome: {usuario['nome']}\n> ID: {usuario["id_usuario"]}\n> Livros emprestados: {usuario['livros_emprestados']}")
    else:
        print(">>>>> USUARIO NÃO ENCONTRADO <<<<<")


# Função para mostrar o relatório de todos os usuários

def mostrar_relatorio_todos_usuarios():
    if usuarios:
        for id_usuario, usuario in usuarios.items():
            print(
                f"\n> Nome: {usuario['nome']}\n> ID: {usuario['id_usuario']}\n> Livros emprestados: {usuario['livros_emprestados']}")
    else:
        print(">>>>> NENHUM USUARIO CADASTRADO <<<<<")





# Função que deixa o menu principal em loop

def menu_principal():
    while True:
        print("\n>>> Menu Principal <<<")
        print("1 - Adicionar Livro")
        print("2 - Adicionar Usuário")
        print("3 - Emprestar Livro")
        print("4 - Devolver Livro")
        print("5 - Relatório de um Livro")
        print("6 - Relatório de Todos os Livros")
        print("7 - Relatório de um Usuário")
        print("8 - Relatório de Todos os Usuários")
        print("9 - Sair")

        opcao = input("Escolha uma opção: \n>> ")

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
            print("Saindo do menu principal...")
            adicionar_ao_dicionario(livros, 'novo_id', {'titulo': 'Novo Livro', 'autor': 'Autor Desconhecido', 'disponivel': True, 'usuario': None})
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_inicial():
    while True:
        print("\n>>> Biblioteca <<<")
        print("1 - Estante de Livros")
        print("2 - Acessar Menu Principal")
        print("3 - Fechar Biblioteca")

        opcao = input("Escolha uma opção: \n>> ")

        if opcao == "1":
            acessar_biblioteca()
        elif opcao == "2":
            menu_principal()
        elif opcao == "3":
            print("\nFechando biblioteca...\n")
            adicionar_ao_dicionario(livros, 'novo_id', {'titulo': 'Novo Livro', 'autor': 'Autor Desconhecido', 'disponivel': True, 'usuario': None})
            break
        else:
            print("Digite uma opção valida.")

# Ativa o menu principal
menu_inicial()