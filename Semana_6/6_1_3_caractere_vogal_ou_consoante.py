import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

caractere = input("Digite um caractere: ")

# Verifica se o input tem mais de um caractere e pede uma nova entrada
while len(caractere) != 1:
    print("Por favor, digite apenas um caractere.")
    caractere = input("Digite um caractere: ")

# Verifica se o caractere é uma letra do alfabeto
if caractere.isalpha():
    vogais = 'aeiouAEIOU'
    if caractere in vogais:
        print(f"{caractere} é uma vogal.")
    else:
        print(f"{caractere} é uma consoante.")
else:
    print("Por favor, insira apenas letras do alfabeto.")