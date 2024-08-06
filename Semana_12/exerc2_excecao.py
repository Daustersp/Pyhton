
import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita e valida o primeiro número
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        break  # Sai do loop se a entrada for válida
    except ValueError:
        print("Oops! Parece que você não digitou um número válido. Por favor, tente novamente.")

# Solicita e valida o segundo número
while True:
    try:
        num2 = float(input("Digite o segundo número: "))
        break  # Sai do loop se a entrada for válida
    except ValueError:
        print("Oops! Parece que você não digitou um número válido. Por favor, tente novamente.")

# Soma os números
soma = num1 + num2

# Mostra o resultado
print(f"A soma de {num1} e {num2} é {soma}.")