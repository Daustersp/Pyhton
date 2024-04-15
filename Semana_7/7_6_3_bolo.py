import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração


class Bolo:
    def __init__(self, nome, peso, recheio, data_vencimento):
        self.nome = nome
        self.peso = peso
        self.recheio = recheio
        self.data_vencimento = data_vencimento

    def exibir_informacoes(self):
        print("Nome do bolo:", self.nome)
        print("Peso do bolo:", self.peso, "gramas")
        print("Recheio do bolo:", self.recheio)
        print("Data de vencimento do bolo:", self.data_vencimento)


# Criando objetos para a classe Bolo
bolo1 = Bolo("Bolo de chocolate", 500, "brigadeiro", "15/04/2024")
bolo2 = Bolo("Bolo de morango", 750, "chantilly", "20/04/2024")

# Exibindo informações dos bolos
print("Informações dos bolos:")
print("------------------------")
print("Bolo 1:")
bolo1.exibir_informacoes()
print("------------------------")
print("Bolo 2:")
bolo2.exibir_informacoes()