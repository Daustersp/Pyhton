import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro para calcular o fatorial: "))

# Inicializa o fatorial como 1
fatorial = 1

# Calcula o fatorial do número
for i in range(1, numero + 1):
    fatorial *= i

# Exibe o fatorial calculado
print(f"O fatorial de {numero} é: {fatorial}")