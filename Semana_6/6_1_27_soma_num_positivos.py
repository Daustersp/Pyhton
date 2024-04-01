import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Inicializa a variável para armazenar a soma dos números positivos
soma_positivos = 0

# Solicita ao usuário que insira 30 números
for i in range(30):
    numero = float(input(f"Digite o {i+1}º número: "))
    if numero > 0:
        soma_positivos += numero

# Exibe a soma dos números positivos
print(f"A soma dos números positivos é: {soma_positivos}")