import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita ao usuário que insira os valores dos lados do triângulo
lado_a = float(input("Digite o valor do lado A: "))
lado_b = float(input("Digite o valor do lado B: "))
lado_c = float(input("Digite o valor do lado C: "))

# Verifica se os valores formam um triângulo
if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print("Os valores formam um triângulo.")
else:
    print("Os valores não formam um triângulo.")