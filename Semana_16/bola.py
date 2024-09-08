import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        """Altera a cor da bola para a nova cor fornecida."""
        self.cor = nova_cor

    def mostraCor(self):
        """Exibe a cor atual da bola."""
        return self.cor

# Solicitar ao usuário os atributos da bola
cor_inicial = input("Digite a cor inicial da bola: ")
circunferencia = float(input("Digite a circunferência da bola (em cm): "))
material = input("Digite o material da bola: ")
    
# Criando uma instância de Bola com os atributos fornecidos
minha_bola = Bola(cor=cor_inicial, circunferencia=circunferencia, material=material)
    
# Mostrando a cor inicial
print(f"A cor inicial da bola é: {minha_bola.mostraCor()}")
    
# Solicitar a nova cor ao usuário
nova_cor = input("Digite a nova cor da bola: ")
    
# Alterar a cor da bola
minha_bola.trocaCor(nova_cor)
    
# Mostrar a nova cor
print(f"A nova cor da bola é: {minha_bola.mostraCor()}")