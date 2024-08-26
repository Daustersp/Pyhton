# Herança

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

class Atleta:
    def __init__(self, peso, aposentado=False):
        self.peso = peso
        self.aposentado = aposentado

    def aposentar(self):
        self.aposentado = True
        print("Atleta aposentado.")

    def aquecer(self):
        print("Atleta aquecendo.")

class Corredor(Atleta):
    def correr(self):
        if not self.aposentado:
            print("Corredor correndo.")
        else:
            print("O corredor está aposentado e não pode correr.")

class Nadador(Atleta):
    def nadar(self):
        if not self.aposentado:
            print("Nadador nadando.")
        else:
            print("O nadador está aposentado e não pode nadar.")

class Ciclista(Atleta):
    def pedalar(self):
        if not self.aposentado:
            print("Ciclista pedalando.")
        else:
            print("O ciclista está aposentado e não pode pedalar.")

# Código de teste

# Criar instâncias de cada classe
corredor = Corredor(peso=70)
nadador = Nadador(peso=75)
ciclista = Ciclista(peso=80)

# Testar métodos dos objetos
print("Testando Corredor:")
corredor.aquecer()
corredor.correr()

print("\nTestando Nadador:")
nadador.aquecer()
nadador.nadar()

print("\nTestando Ciclista:")
ciclista.aquecer()
ciclista.pedalar()

# Aposentar um atleta e testar novamente
print("\nAposentar Corredor e testar novamente:")
corredor.aposentar()
corredor.correr()