class Livro:
    def __init__(self, titulo, autor, disponivel, usuario, id):
        self._titulo = titulo or ""
        self._autor = autor or ""
        self._disponivel = disponivel or True
        self._usuario = usuario or ""
        self._id = id or 0

    # pegar o livro ela registra o id do usuario no livro e o coloca o livro
    # como indisponivel

    def pegarlivro(self, user_id):
        self._usuario = user_id
        self._disponivel = False

    def devolverlivro(self):
        self._usuario = ""
        self._disponivel = True

    def get_data(self):
        return{
            'titulo': self._titulo,
            'autor': self._autor,
            'disponivel':self._disponivel,
            'usuario':self._usuario,
            'id':self._id,
        }