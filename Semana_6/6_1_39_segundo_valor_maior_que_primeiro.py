import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Lê os dois valores
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor (maior que o primeiro): "))

# Inicializa a variável para armazenar a soma
soma = 0

# Loop para somar os inteiros entre os valores
for i in range(valor1, valor2 + 1):
    soma += i

# Imprime a soma
print(f"A soma dos inteiros entre {valor1} e {valor2} é: {soma}")