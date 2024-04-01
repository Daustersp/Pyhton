import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita ao usuário que digite um número
numero = int(input("Digite um número: "))

# Verifica se o número é múltiplo de 5
if numero % 5 == 0:
    print(f"O número {numero} é múltiplo de 5.")
else:
    print(f"O número {numero} não é múltiplo de 5.")