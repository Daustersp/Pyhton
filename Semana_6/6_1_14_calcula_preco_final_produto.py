import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita ao usuário que insira o preço original do produto e o desconto
preco_original = float(input("Digite o preço original do produto: R$ "))
desconto = float(input("Digite o desconto (%): "))

# Calcula o preço final com o desconto
preco_final = preco_original - (preco_original * (desconto / 100))

# Exibe o preço final do produto
print(f"O preço final do produto com desconto é: R$ {preco_final:.2f}")