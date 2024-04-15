import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Listas para armazenar os números inteiros pares e ímpares
numeros = []
pares = []
impares = []

# Loop para ler os números
for i in range(20):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Mostrando as listas de números pares e ímpares
print("Números pares:", pares)
print("Números ímpares:", impares)
