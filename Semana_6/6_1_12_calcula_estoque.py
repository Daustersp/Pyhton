import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita ao usuário que insira as informações sobre o estoque do produto
quantidade_atual = int(input("Digite a quantidade atual em estoque do produto: "))
quantidade_maxima = int(input("Digite a quantidade máxima em estoque do produto: "))
quantidade_minima = int(input("Digite a quantidade mínima em estoque do produto: "))

# Calcula a quantidade média em estoque
quantidade_media = (quantidade_maxima + quantidade_minima) / 2

# Verifica se a quantidade em estoque é maior ou igual à quantidade média
if quantidade_atual >= quantidade_media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")