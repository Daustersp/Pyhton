# A estrutura básica da Python range é:

# range([start], [stop], [step])

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

num = int(input("Digite um número: "))
if num > 0:
    for num in range(1,num+1,1):
        print(num)

while num < 1:
    num = int(input("Número digitado não é maior que 0.\nEscolha outro número: "))
    for num in range(1,num+1,1):
        print(num)