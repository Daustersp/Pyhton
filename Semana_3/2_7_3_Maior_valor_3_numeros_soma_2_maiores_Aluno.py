import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if ((num1>num2) and (num1>num3)):
    maior = num1
    if (num2 > num3):
        maior2 = num2
    else:
        maior2 = num3
elif ((num2>num1) and (num2>num3)):
    maior = num2
    if (num1 > num3):
        maior2 = num1
    else:
        maior2 = num3
    
else:
    maior = num3
    if (num2 > num1):
        maior2 = num2
    else:
        maior2 = num1
soma = maior + maior2
print("A soma dos dois meiores números é ", soma)