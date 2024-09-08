import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    def adiciona_cidade(self, cidade):
        cidade.estado = self
        self.cidades.append(cidade)

    def população(self):
        return sum([c.população for c in self.cidades])


class Cidade:
    def __init__(self, nome, população):
        self.nome = nome
        self.população = população
        self.estado = None

    def __str__(self):
        return f"Cidade (nome={self.nome}, população={self.população}, estado={self.estado})"

# Populações obtidas no site da Wikipédia
# IBGE estimativa 2022
ro = Estado("Rondônia", "RO")
ro.adiciona_cidade(Cidade("Porto Velho", 460413))
ro.adiciona_cidade(Cidade("Cacoal", 97637))
ro.adiciona_cidade(Cidade("Vilhena", 124333))

sp = Estado("São Paulo", "SP")
sp.adiciona_cidade(Cidade("São Paulo", 21518955))
sp.adiciona_cidade(Cidade("Guarulhos", 1291784))
sp.adiciona_cidade(Cidade("Campinas", 1173370))

rj = Estado("Rio de Janeiro", "RJ")
rj.adiciona_cidade(Cidade("Rio de Janeiro", 12936629))
rj.adiciona_cidade(Cidade("São Gonçalo", 960652))
rj.adiciona_cidade(Cidade("Duque de Caixias", 808152))

for estado in [ro, sp, rj]:
    print(f"Estado: {estado.nome} Sigla: {estado.sigla}")
    for cidade in estado.cidades:
        print(f"Cidade: {cidade.nome} População: {cidade.população}")
    print(f"População do Estado: {estado.população()}\n")
