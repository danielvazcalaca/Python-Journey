usuarios_cadastrados = {}
livros_cadastrados = {}


def cadastrando_usuario():
    usuario = input("Qual o seu usuario?")
    if usuario in usuarios_cadastrados:
        print("Usuario já cadastrado")
    else:
        adicionar_usuario = input("Usuario não cadastrado, digite o nome que deseja cadastrar! ")
        usuarios_cadastrados[adicionar_usuario] = adicionar_usuario
        print("Usuario Cadastrado!")


def cadastrando_livro():
    livro = print("Qual o nome do livro que você deseja cadastrar?")
    if livro in livros_cadastrados:
        print("Esse livro já está cadastrado.")
    else:
        print("Seu livro foi cadastrado")

#
#

while True:
    print("1 - Usuario")
    print("2 - Cadastrar Livro")
    print("3 - Olhar Livros Cadastrados")
    print("4 - Olhar Usuarios Cadastrados")
    print("9 - Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        cadastrando_usuario()
    elif escolha == "2":
        cadastrando_livro()
    elif escolha == "3":
        print(cadastrado_livro)
    elif escolha == "4":
        print(usuarios_cadastrados)
    elif escolha == "9":
        print("Tchau")
        break
    else:
        print("Digite um numero de 1 a 9")