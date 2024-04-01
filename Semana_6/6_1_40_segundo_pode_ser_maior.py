import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Lê os dois valores
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

# Determina os valores mínimo e máximo
minimo = min(valor1, valor2)
maximo = max(valor1, valor2)

# Inicializa a variável para armazenar a soma
soma = 0

# Loop para somar os inteiros entre os valores
for i in range(minimo, maximo + 1):
    soma += i

# Imprime a soma
print(f"A soma dos inteiros entre {minimo} e {maximo} é: {soma}")