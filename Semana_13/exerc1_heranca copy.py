# Herança

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"Valor do ingresso: R$ {self.valor:.2f}")


class VIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)  # Chama o construtor da classe base Ingresso
        self.adicional = adicional

    def valorVIP(self):
        return self.valor + self.adicional

    def imprimeValor(self):
        print(f"Valor do ingresso VIP: R$ {self.valorVIP():.2f}")


# Exemplo de uso
ingresso_normal = Ingresso(100.00)
ingresso_normal.imprimeValor()

ingresso_vip = VIP(100.00, 50.00)
ingresso_vip.imprimeValor()