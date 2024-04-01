import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Inicializa a variável para armazenar a soma dos valores
soma_valores = 0

# Solicita ao usuário que insira 10 valores
for i in range(10):
    valor = float(input(f"Digite o {i+1}º valor: "))
    soma_valores += valor

# Calcula a média dos valores
media = soma_valores / 10

# Exibe a média dos valores
print(f"A média dos valores é: {media}")
