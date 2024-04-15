import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Lista para armazenar os números reais
numeros = []

# Loop para ler os números
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número real: "))
    numeros.append(numero)

# Invertendo a ordem dos elementos na lista
numeros.reverse()

# Mostrando a lista na ordem inversa
print(numeros)
