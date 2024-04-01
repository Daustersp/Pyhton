import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita ao usuário que insira uma sequência de números inteiros separados por espaço
entrada = input("Digite uma sequência de números inteiros separados por espaço: ")

# Separa os números e converte cada um para inteiro
numeros = [int(numero) for numero in entrada.split()]

# Filtra apenas os números pares
pares = [numero for numero in numeros if numero % 2 == 0]

# Exibe os números pares
if pares:
    print("Números pares encontrados:", pares)
else:
    print("Não foram encontrados números pares.")