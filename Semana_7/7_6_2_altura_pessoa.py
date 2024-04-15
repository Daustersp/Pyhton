import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração


class Pessoa:
    def __init__(self, altura_metros, peso_kg, temperatura_corporal, sexo):
        self.altura_metros = altura_metros
        self.peso_kg = peso_kg
        self.temperatura_corporal = temperatura_corporal
        self.sexo = sexo
        # Calculando a altura em milímetros
        self.altura_mm = altura_metros * 1000

    def exibir_informacoes(self):
        print("Altura:", self.altura_metros, "metros")
        print("Peso:", self.peso_kg, "quilos")
        print("Temperatura corporal:", self.temperatura_corporal, "°C")
        print("Sexo:", self.sexo)
        print("Altura em milímetros:", self.altura_mm, "milímetros")


# Criando objetos para a classe Pessoa
pessoa1 = Pessoa(1.75, 70, 36.5, "masculino")
pessoa2 = Pessoa(1.60, 55, 37.0, "feminino")

# Exibindo informações das pessoas
print("Informações das pessoas:")
print("------------------------")
print("Pessoa 1:")
pessoa1.exibir_informacoes()
print("------------------------")
print("Pessoa 2:")
pessoa2.exibir_informacoes()