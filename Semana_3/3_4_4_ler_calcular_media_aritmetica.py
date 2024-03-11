# A estrutura básica da Python range é:

# range([start], [stop], [step])

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração
soma = 0
for _ in range(10):
    valor = int(input("Digite um valor: "))
    soma = soma + valor

media = float(soma / 10)

print("A média aritmética dos númetos digitados é: ", media)