# CRIAR SUPERCLASSE ANIMAL
class Animal:
    def __init__(self):
        pass

    def emitir_som(self):
        pass

# CRIAR SUBCLASSES HOMEM, CACHORRO, GATO E PATO
class Homem(Animal):
    def __init__(self):
        Animal.__init__(self)

    def emitir_som(self):
        print("Oi") 

class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)

    def emitir_som(self):
        print("au..au") 

class Gato(Animal):
    def __init__(self):
        Animal.__init__(self)

    def emitir_som(self):
        print("miau..miau") 

class Pato(Animal):
    def __init__(self):
        Animal.__init__(self)

    def emitir_som(self):
        print("quack..quack") 

# TESTAR CLASSES
h = Homem()
c = Cachorro()
g = Gato()
p = Pato()


# INVOCANDO O MÉTODO SAUDAR COM O CONCEITO DE POLIMORFISMO
h.emitir_som()
c.emitir_som()
g.emitir_som()
p.emitir_som()
