livros = {}
usuarios = {}

#
# Adicionar Livro
#

def adicionar_livro():
    livro = input("Qual livro deseja adicionar?")
    if livro in livros:
        print("Este livro já existe!")
    else:
        livros[livro] = livro
        print(f"Livro adicionado com sucesso! ({livro})")

#
# Adicionar Usuario
#

def adicionar_usuario():
    usuario = input("Qual usuario deseja adicionar?")
    if usuario in usuarios:
        print(f"O usuario {usuario} já existe!")
    else:
        usuarios[usuario] = usuario
        print(f"Usuario adicionado com sucesso! ({usuario})")



def menu_principal():
    while True:
        print("\n/// Biblioteca ///")
        print("1 - Adicionar Livro")
        print("2 - Adicionar Usuário")
        print("3 - Mostrar Relatório de um Livro")
        print("4 - Mostrar Relatório de um Usuário")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            adicionar_usuario()
        elif opcao == "3":
            mostrar_relatorio_livro()
        elif opcao == "4":
            mostrar_relatorio_usuario()
        elif opcao == "5":
            mostrar_relatorio_livro()
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")


# Menu
menu_principal()
