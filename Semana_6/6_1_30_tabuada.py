import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita ao usuário que insira um número
numero = int(input("Digite um número para ver sua tabuada: "))

# Calcula e exibe a tabuada do número de 1 até 10
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")