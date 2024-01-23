''' Programa que leia a idade de uma pessoa em anos e apresente uma mensagem
identificando se é maior ou menor de 18 anos '''


import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração


idade = int(input("Digite a idade desejada: "))
if idade >=18:
    print("A idade informada é de alguém possui 18 anos ou mais")
else:
    print("A idade informada é de alguém com idade inferior a 18 anos")