# A estrutura básica da Python range é:

# range([start], [stop], [step])

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

texto = input("Digite um texto: ")
if ("@" in texto):
    print("@ encontrado")
else:
    print("e-mail inválido")