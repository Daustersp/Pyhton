# A estrutura básica da Python range é:

# range([start], [stop], [step])

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

cont_negativos = 0
for _ in range(10):
    valor = float(input("Digite um valor: "))
    if valor < 0:
        cont_negativos += 1 #ou cont_netavivos = cont_negativos + 1

print("A quantidade de números negativos foi: ", cont_negativos)