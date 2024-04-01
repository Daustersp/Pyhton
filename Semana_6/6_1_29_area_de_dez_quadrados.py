import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Define uma função para calcular a área de um quadrado
def calcular_area_quadrado(lado):
    return lado ** 2

# Solicita ao usuário que insira o lado de 10 quadrados e calcula e exibe a área de cada um
for i in range(1, 11):
    lado = float(input(f"Digite o lado do {i}º quadrado: "))
    area = calcular_area_quadrado(lado)
    print(f"A área do {i}º quadrado é: {area}")