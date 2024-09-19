class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            print('Erro')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            print('Plano Trocado')
            self.plano = novo_plano
        else:
            print('Plano Negado')

    # def ver_filme(self, assistir_filme):




cliente = Cliente('Daniel', 'aboboraquadrada@hotmail.com', 'basic')
print(cliente.plano)
cliente.mudar_plano(input())
print(cliente.plano)