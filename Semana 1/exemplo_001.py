# Programa para ler um número inteiro e escrever o seu antecessor e seu sucessor
# Variáveis utilizadas - num, antecessor, sucessor

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

num = int(input("Digite um número: "))
antecessor = int(num - 1)
sucessor = int(num + 1)
print("O antecessor é o número: ", antecessor) 
print("O sucessor é o número: ", sucessor)
