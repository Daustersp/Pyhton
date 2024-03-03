# A estrutura básica da Python range é:

# range([start], [stop], [step])

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Exemplo1 - Digitar 10 valores solicitados ao usuário
for i in range(10):
   valor = int(input(f'Digite o valor {i}: '))

# Exemplo 2 - verificar se o valor digitado é positivo, negativo ou zero
# for i in range(10):
#     valor = int(input(f'Digite o valor {i}: '))
#     if valor > 0:
#         print("Positivo")
#     elif valor < 0: 
#         print("Negativo")
#     else:
#         print("Zero")


# Exemplo 3
# positivos = negativos = zeros = 0 #atribuir zero às variáveis para somar posteriormente
# positivos = 0
# negativos = 0
# zeros = 0

# for i in range(10):
#     valor = int(input(f'Digite o valor {i}: '))
#     if valor > 0:
#         positivos+=1
#     elif valor < 0: 
#         negativos+=1
#     else:
#         zeros+=1
        
# print(" Quantidade de números positivos:", positivos)
# print(" Quantidade de números negativos:", negativos)
# print(" Quantidade de números zeros:", zeros)