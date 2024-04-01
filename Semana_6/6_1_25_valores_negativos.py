import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Inicializa o contador de valores negativos
contador_negativos = 0

# Solicita ao usuário que insira 10 valores
for i in range(10):
    valor = float(input(f"Digite o {i+1}º valor: "))
    if valor < 0:
        contador_negativos += 1

# Exibe a quantidade de valores negativos
print(f"O número de valores negativos é: {contador_negativos}")
