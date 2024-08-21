# Herança

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# CLASSE PAI
class Animal():
    def __init__(self, nome, cor):
        self.__nome = nome
        self.__cor = cor

    def comer(self):
        print(f"O {self.__nome} está comendo")


# CLASSES FILHAS
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)


gato = Gato("Bichano", "Branco")
cachorro = Cachorro("Totó", "Preto")
coelho = Coelho("Pernalonga", "Cinza")

gato.comer()
cachorro.comer()
coelho.comer()
