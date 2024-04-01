import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Inicializa as variáveis para armazenar a soma e o contador dos números positivos
soma_positivos = 0
contador_positivos = 0

# Solicita ao usuário que insira 20 números
for i in range(20):
    numero = float(input(f"Digite o {i+1}º número: "))
    if numero > 0:
        soma_positivos += numero
        contador_positivos += 1

# Verifica se foram inseridos números positivos para evitar divisão por zero
if contador_positivos > 0:
    media_positivos = soma_positivos / contador_positivos
    print(f"A média dos números positivos é: {media_positivos}")
else:
    print("Nenhum número positivo foi inserido.")