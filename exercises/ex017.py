class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == "+":
            return("Aumentar o Canal")
        elif botao == "-":
            return("Diminuir o Canal")
        else:
            return("Botão Errado")



controle_remoto1 = ControleRemoto("branco", "3m", "9cm", "20km")
print(controle_remoto1.cor, controle_remoto1.altura, controle_remoto1.profundidade, controle_remoto1.largura)

controle_remoto2 = ControleRemoto("Azul", "2m", "10m", "30km")
print("\n" + controle_remoto2.cor, controle_remoto2.altura, controle_remoto2.profundidade, controle_remoto2.largura)

resultado = controle_remoto1.passar_canal("+")
print(resultado)
