import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Inicializa a variável para armazenar a soma e o contador de números
soma = 0
contador = 0

# Loop para somar os números inteiros entre 15 e 100
for i in range(15, 101):
    soma += i
    contador += 1

# Calcula a média aritmética
media = soma / contador

# Imprime a média aritmética
print(f"A média aritmética dos números entre 15 e 100 é: {media}")