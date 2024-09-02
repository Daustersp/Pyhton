# Herança

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Criando uma classe - PAI
# class Pessoa():
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def saudacao(self):
#         print(f"Meu nome é {self.nome} e tenho {self.idade} anos")

# #Criando um objeto a partir da superclasse
# pessoa1 = Pessoa("Fred Flintstone", 100)
# pessoa1.saudacao()


# # Criando uma subclasse - Slide 9 / Slide 10
# class Aluno(Pessoa):
#     pass

# #Criando um objeto a partir da subclasse
# pessoa2 = Aluno("Maria da Silva", 20)
# pessoa2.saudacao()

# SLIDE 12 - CRIANDO ATRIBUTOS E MÉTODOS ESPECÍFICOS

# CRIANDO UMA CLASSE - PAI
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos")

#Criando um objeto a partir da superclasse
pessoa1 = Pessoa("Fred Flintstone", 100)
pessoa1.saudacao()

# Criando uma subclasse - Professor(Pessoa):
class Professor(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def mostrarcurso(self):
        super().saudacao()
        print(f"e ministra o curso de {self.curso}")

#Criando objetos a partir da subclasse
pessoa3 = Professor("Dauster Souza Pereira", 40, "POO")
pessoa3.saudacao()
pessoa3.mostrarcurso()