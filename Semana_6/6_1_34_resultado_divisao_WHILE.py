import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita ao usuário que insira os dois valores
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor (não pode ser zero): "))

# Enquanto o segundo valor for zero, solicita um novo valor
while valor2 == 0:
    print("O segundo valor não pode ser zero.")
    valor2 = float(input("Digite um novo valor para o segundo número: "))

# Calcula e imprime o resultado da divisão
resultado = valor1 / valor2
print(f"O resultado da divisão de {valor1} por {valor2} é: {resultado}")