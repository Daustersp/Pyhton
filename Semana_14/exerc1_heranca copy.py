# Herança

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# SUPERCLASSE / BASE / PAI
class Ingresso:
    def __init__(self, valor): #definição do construtor
        self.valor = valor

    def imprimeValor(self): #método para imprimir o valor
        print(f"Valor do ingresso: R$ {self.valor:.2f}") #definição com 2 casas decimais

# SUBCLASSE / DERIVADA / FILHA
class VIP(Ingresso): #indico o nome da subclasse e o nome da superclasse PAI
    def __init__(self, valor, adicional):
        super().__init__(valor)  # Chama o construtor da classe base Ingresso
        self.adicional = adicional

    def valorVIP(self): #método para calcular o valor do ingresso VIP
        return self.valor + self.adicional

    def imprimeValor(self):
        print(f"Valor do ingresso VIP: R$ {self.valorVIP():.2f}")


# Exemplo de uso
ingresso_normal = Ingresso(100.00)
ingresso_normal.imprimeValor()

ingresso_vip = VIP(100.00, 50.00)
ingresso_vip.imprimeValor()