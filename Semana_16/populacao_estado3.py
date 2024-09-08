import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

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

# Criando cidades
cidade1 = Cidade("São Paulo", 12300000)
cidade2 = Cidade("Campinas", 1210000)
cidade3 = Cidade("Santos", 430000)

cidade4 = Cidade("Rio de Janeiro", 6748000)
cidade5 = Cidade("Niterói", 500000)

cidade6 = Cidade("Belo Horizonte", 2520000)
cidade7 = Cidade("Uberlândia", 700000)

# Criando estados
estado1 = Estado("São Paulo", "SP")
estado2 = Estado("Rio de Janeiro", "RJ")
estado3 = Estado("Minas Gerais", "MG")

# Adicionando cidades aos estados
estado1.adicionar_cidade(cidade1)
estado1.adicionar_cidade(cidade2)
estado1.adicionar_cidade(cidade3)

estado2.adicionar_cidade(cidade4)
estado2.adicionar_cidade(cidade5)

estado3.adicionar_cidade(cidade6)
estado3.adicionar_cidade(cidade7)

# Exibindo a população total de cada estado
for estado in [estado1, estado2, estado3]:
    print(f"A população do estado {estado.nome} ({estado.sigla}) é {estado.calcular_populacao()}")