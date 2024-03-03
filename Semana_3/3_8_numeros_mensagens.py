import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

#ORDEM DECRESCENTE
#ORDEM CRESCENTE
num1 = int(input('Digite o primeiro número: '))
num2  = int(input('Digite o segundo número : '))

if(num1 == num2):
    print("Números iguais")
elif (num1 > num2):
    print("Primeiro é maior")
else:
    print("Segundo maior")