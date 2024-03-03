import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if ((num1>num2) and (num1>num3)):
    maior = num1
    
elif ((num2>num1) and (num2>num3)):
    maior = num2
    
else:
    maior = num3

print("O maior número é ", maior)



# Informando que existem números iguais

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# num3 = int(input("Digite o terceiro número: "))
# if ((num1>num2) and (num1>num3)):
#     print ("O maior número é o ", num1)
# elif ((num2>num1) and (num2>num3)):
#    print("O maior número é o ", num2)
# elif ((num3>num1) and (num3>num2)):
#    print("O maior número é o ", num3)
# else:
#    print("Existem números iguais!")