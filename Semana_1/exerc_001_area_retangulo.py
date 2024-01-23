# Programa para calcular a área do retângulo
# Variáveis utilizadas - area, base, altura, real

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

base = int(input("Digite o valor da base: "))
altura = int(input("Digite o valor da altura: ")) 
area = base * altura
print("A área do retângulo é", area)
