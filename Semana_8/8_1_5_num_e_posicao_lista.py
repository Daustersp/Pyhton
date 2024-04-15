import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

numeros = []

# Loop para ler os números
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Mostrando cada número com sua posição na lista
print("Números e suas posições na lista:")
for posicao, numero in enumerate(numeros, start=1):
    print(f"Posição {posicao}: {numero}")