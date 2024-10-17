from biblioteca import Biblioteca

def menu_principal():

    b = Biblioteca()

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
            b.adicionarlivro()
        elif opcao == '2':
            b.adicionarusuario()
        elif opcao == '3':
            b.emprestarlivro()
        elif opcao == '4':
            b.devolverlivro()
        elif opcao == '5':
            b.mostrar_relatorio_livro()
        elif opcao == '6':
            b.mostrar_relatorio_de_todos_os_livros()
        elif opcao == '7':
            b.mostrar_relatorio_usuarios()
        elif opcao == '8':
            b.mostrar_relatorio_todos_os_usuarios()
        elif opcao == '9':
            print("Saindo do menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()