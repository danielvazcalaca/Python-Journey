cadastrado_usuario = {}
cadastrado_livro = {}


def usuario_cadastrado():
    user = input("What is your username?")
    if user in cadastrado_usuario:
        print("Usuario já cadastrado")
    else:
        print("Vamos Criar um usuario!")
        adicionar_usuario = input("Digite o nome que você deseja: ")


cadastrado_usuario = {}
cadastrado_livro = {}


def usuario_cadastrado():
     user = input("What is your username?")
     if user in cadastrado_usuario:
          print("Usuario já cadastrado")
     else:
          print("Vamos Criar um usuario!")
          adicionar_usuario = input("Digite o nome que você deseja: ")


def livro_cadastrado():
     print(12312312)


while True:
     print("1 - Usuario")
     print("2 - Cadastrar Livro")
     print("3 - Olhar Livros Cadastrados")
     print("4 - Olhar Usuarios Cadastrados")
     print("9 - Sair")
     escolha = input("Escolha uma opção: ")
     if escolha == "1":
          username()
     elif escolha == "2":
          livro_cadastrado()
     elif escolha == "3":
          print(cadastrado_livro)
     elif escolha == "4":
          print(cadastrado_usuario)
     elif escolha == "9":
          print("Tchau")
          break
     else:
          print("Digite um numero de 1 a 9")

def livro_cadastrado():
    print(12312312)


while True:
    print("1 - Usuario")
    print("2 - Cadastrar Livro")
    print("3 - Olhar Livros Cadastrados")
    print("4 - Olhar Usuarios Cadastrados")
    print("9 - Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        username()
    elif escolha == "2":
        livro_cadastrado()
    elif escolha == "3":
        print(cadastrado_livro)
    elif escolha == "4":
        print(cadastrado_usuario)
    elif escolha == "9":
        print("Tchau")
        break
    else:
        print("Digite um numero de 1 a 9")