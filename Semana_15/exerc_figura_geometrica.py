# Polimorfismo

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# CRIAR SUPERCLASSE FIGURA GEOMÉTRICA
class FiguraGeometrica:
    def __init__(self, nome):
        self.nome = nome

    def calcula_area(self):
        pass

# CRIAR SUBCLASSES QUADRADO, CIRCULO, E TRIÂNGULO
class Quadrado(FiguraGeometrica):
    def __init__(self, lado):
        FiguraGeometrica.__init__(self, "Quadrado")
        self.lado = lado

    def calcula_area(self):
        return self.lado ** 2

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        FiguraGeometrica.__init__(self, "Triangulo")
        self.base = base
        self.altura = altura

    def calcula_area(self):
        return (self.base * self.altura) / 2
    
class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        FiguraGeometrica.__init__(self, "Circulo")
        self.raio = raio

    def calcula_area(self):
        return 3.14 * (self.raio ** 2)
    
# TESTAR CLASSES
quadrado = Quadrado(2)
triangulo = Triangulo(2, 5)
circulo = Circulo(5)


# INVOCANDO O MÉTODO SAUDAR COM O CONCEITO DE POLIMORFISMO
print(quadrado.calcula_area())
print(triangulo.calcula_area())
print(circulo.calcula_area())