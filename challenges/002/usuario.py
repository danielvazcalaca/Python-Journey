class Usuario:
    def __init__(self, nome, cpf, nascimento, id_usuario):
        self._nome = nome or ""
        self._cpf = cpf or ""
        self._id_livro = ""
        self._nascimento = nascimento or ""
        self._id_usuario = id_usuario or 0

    def pegarlivro(self, id_livro):
        self._id_livro = id_livro

    def devolverlivro(self):
        self._id_livro = ""

    def get_data(self):
        return {
            "nome": self._nome,
            "cpf": self._cpf,
            "id_livro": self._id_livro,
            "nascimento": self._nascimento,
            "id_usuario": self._id_usuario,
        }