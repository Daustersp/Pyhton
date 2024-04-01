import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Inicializa o contador de valores maiores ou iguais a 5
contador = 0

# Solicita ao usuário que insira 20 valores
for i in range(20):
    valor = float(input(f"Digite o {i+1}º valor: "))
    if valor >= 5:
        contador += 1

# Exibe a quantidade de valores maiores ou iguais a 5
print(f"O número de valores maiores ou iguais a 5 é: {contador}")
