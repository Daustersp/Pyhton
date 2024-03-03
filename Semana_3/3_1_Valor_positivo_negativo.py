import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

num = int(input("Digite um número: "))
if (num>0):
    print ("O valor digitado é positivo")
elif (num < 0):
    print("O valor digitado é negativo")
else:
    print ("O valor digitado é igual a zero")