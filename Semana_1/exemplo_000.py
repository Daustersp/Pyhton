# Programa para calcular a média de 4 números inteiros
# Variáveis utilizadas - n1, n2, n3, n4, media

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o 4º número: "))
media = float((n1+n2+n3+n4)/4) 
print("A média é", media)
