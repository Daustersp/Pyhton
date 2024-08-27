# Herança

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# CRIAR SUPERCLASSE IDIOMA
class Idioma:
    def __init__(self):
        pass

    def saudar(self):
        pass

# CRIAR SUBCLASSES PORTUGUÊS, MANDARIM, ALEMÃO E FRANCÊS
class Portugues(Idioma):
    def __init__(self): #m método construtor da classe Portugues
        Idioma.__init__(self) #invocar o método construtor da superclasse

    def saudar(self):
        print("Oi") #como o método é void, não precisa devolver nada. Só dar um print na mensagem


class Mandarim(Idioma):
    def __init__(self): #m método construtor da classe Mandarim
        Idioma.__init__(self) #invocar o método construtor da superclasse

    def saudar(self):
        return "Ni hao" # utiliza o return porque devolve uma string
    
class Alemao(Idioma):
    def __init__(self): #m método construtor da classe Alemão
        Idioma.__init__(self) #invocar o método construtor da superclasse

    def saudar(self):
        return "Hallo" # utiliza o return porque devolve uma string
    
class Frances(Idioma):
    def __init__(self): #m método construtor da classe Alemão
        Idioma.__init__(self) #invocar o método construtor da superclasse

    def saudar(self):
        return "Salut" # utiliza o return porque devolve uma string
    
# TESTAR CLASSES
p = Portugues()
m = Mandarim()
a = Alemao()
f = Frances()


# INVOCANDO O MÉTODO SAUDAR COM O CONCEITO DE POLIMORFISMO
p.saudar()
print(m.saudar())
print(a.saudar())
print(f.saudar())