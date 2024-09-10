import os
os.system('cls')

class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    def adicionar_cidade(self, cidade):
        self.cidades.append(cidade)

    def calcular_populacao(self):
        return sum(cidade.populacao for cidade in self.cidades)
    

cidade1=Cidade('Osasco', 100500)
cidade2=Cidade('Tabuão', 200200)
cidade3=Cidade('Marília', 300300)

estado1=Estado('São Paulo', 'SP')

estado1.adicionar_cidade(cidade1)
estado1.adicionar_cidade(cidade2)
estado1.adicionar_cidade(cidade3)

# print(f"A população do estado de {estado1.nome} ({estado1.sigla}) é de {estado1.calcular_populacao(cidade1)}")

# Exibindo a população total de cada estado
# for estado in [estado1]:
#     print(f"A população do estado {estado.nome} ({estado.sigla}) é {estado.calcular_populacao()}")


for estado in [estado1]:
    print(f"A população do estado {estado.nome} ({estado.sigla}) é {cidade1.populacao}")
