# A estrutura básica da Python range é:

# range([start], [stop], [step])

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

soma = 0
for i in range(10):
    num = float(input(f"Digite o número {i + 1}: "))
    soma = soma + num

print(f"A soma dos números lidos é: {soma:.1f}")
