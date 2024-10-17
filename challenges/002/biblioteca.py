from livro import Livro
from usuario import Usuario

class Biblioteca:
    def __init__(self):
        self._livros = []
        self._usuarios = []

    def adicionarlivro(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Coloque o nome do autor: ")
        id = input("Digite o ID: ")

        book = Livro(titulo=titulo, autor=autor, id=id, disponivel=True, usuario="")
        self._livros.append(book)
        print("Livro adicionado com sucesso!")

    def adicionarusuario(self):
        nome = input("Digite o nome do usuário: ")
        cpf = input("Digite o CPF do usuário: ")
        nascimento = input("Digite a data de nascimento do usuário: ")
        id = input("Digite o ID do usuário: ")

        user = Usuario(nome=nome, cpf=cpf, nascimento=nascimento, id_usuario=id)
        self._usuarios.append(user)
        print("Usuário adicionado com sucesso!")

    def pesquisarlivro(self):
        titulo = input("Qual o título do livro que deseja emprestar? ")
        for indice, item in enumerate(self._livros):
            if titulo.lower() == item.get_data()['titulo'].lower():
                print(f"Livro encontrado: {titulo}, ")
                return indice
        print("Livro não encontrado.")
        return None

    def pesquisarusuario(self):
        usuario_id = input("Digite o ID do usuário a que deseja emprestar: ")
        for indice, item in enumerate(self._usuarios):
            if usuario_id == item.get_data()["id_usuario"]:
                print(f"Usuário encontrado: ID {usuario_id}")
                return indice
        print("Usuário não encontrado.")
        return None

    def pesquisacompleta(self):
        return self.pesquisarusuario(), self.pesquisarlivro()

    def emprestarlivro(self):
        indice_usuario, indice_livro = self.pesquisacompleta()
        if indice_usuario is not None and indice_livro is not None:
            self._livros[indice_livro].pegarlivro(user_id=self._usuarios[indice_usuario].get_data()["id_usuario"])
            self._usuarios[indice_usuario].pegarlivro(id_livro=self._livros[indice_livro].get_data()["id"])
            print("Livro emprestado com sucesso!")

    def devolverlivro(self):
        indice_usuario, indice_livro = self.pesquisacompleta()
        if indice_usuario is not None and indice_livro is not None:
            self._livros[indice_livro].devolverlivro()
            self._usuarios[indice_usuario].devolverlivro()
            print("Livro devolvido com sucesso!")

    def mostrar_relatorio_livro(self):
        while True:
            titulo = input("Digite o livro que deseja procurar no relatório? (ou digite 'sair' para encerrar): ")

            if titulo.lower() == "sair":
                break
            encontrado = False

            for item in self._livros:
                dados_itens = item.get_data()
                if titulo.lower() in dados_itens['titulo'].lower():
                    print(f"ID: {dados_itens['id']}, Título: {dados_itens['titulo']}, Autor: {dados_itens['autor']}, Disponível: {dados_itens['disponivel']}, Usuário: {dados_itens['usuario']}")
                    encontrado = True

            if not encontrado:
                print("Livro não encontrado.")

    def mostrar_relatorio_de_todos_os_livros(self):
        if not self._livros:
            print("Nenhum livro cadastrado.")
            return
        for item in self._livros:
            dados_itens = item.get_data()
            print(f"ID: {dados_itens['id']}, Título: {dados_itens['titulo']}, Autor: {dados_itens['autor']}, Disponível: {dados_itens['disponivel']}, Usuário: {dados_itens['usuario']}")

    def mostrar_relatorio_usuarios(self):
        while True:
            nome_usuario = input("Qual o usuário que deseja procurar no relatório? (ou digite 'sair' para encerrar): ")

            if nome_usuario.lower() == "sair":
                break
            encontrado = False

            for item in self._usuarios:
                dados_usuario = item.get_data()
                if nome_usuario.lower() in dados_usuario['nome'].lower():
                    print(f"Nome: {dados_usuario['nome']}, CPF: {dados_usuario['cpf']}, Nascimento: {dados_usuario['nascimento']}, ID do Usuário: {dados_usuario['id_usuario']}")
                    encontrado = True

            if not encontrado:
                print("Usuário não encontrado.")

    def mostrar_relatorio_todos_os_usuarios(self):
        if not self._usuarios:
            print("Nenhum usuário cadastrado.")
            return
        for item in self._usuarios:
            dados_usuario = item.get_data()
            print(f"Nome: {dados_usuario['nome']}, CPF: {dados_usuario['cpf']}, Nascimento: {dados_usuario['nascimento']}, ID do Usuário: {dados_usuario['id_usuario']}")
