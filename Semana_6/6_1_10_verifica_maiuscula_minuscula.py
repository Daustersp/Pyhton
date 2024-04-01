import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita ao usuário que insira um caractere
caractere = input("Digite um caractere: ")

# Verifica se o caractere é uma letra
if len(caractere) == 1 and caractere.isalpha():
    if caractere.isupper():
        print(f"O caractere '{caractere}' é uma letra maiúscula.")
    else:
        print(f"O caractere '{caractere}' é uma letra minúscula.")
else:
    print("Por favor, insira apenas um caractere que seja uma letra.")