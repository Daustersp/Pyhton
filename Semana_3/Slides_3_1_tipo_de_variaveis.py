# A estrutura básica da Python range é:

# range([start], [stop], [step])

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# qtde_vendida = 1000
# print(type(qtde_vendida))

# qtde_vendida = 1000
# print("A quantidade vendida foi "+qtde_vendida)

# qtde_vendida = 1000
# custo = 500
# print("A quantidade vendida foi {}".format(qtde_vendida))

# qtde_vendida = 1000
# custo = 500
# print("A quantidade vendida foi {} e o custo {}".format(qtde_vendida,custo))


# if "@" in "dauster.pereira@ifb.edu.br":
#    print("TEM @")
# else:
#    print("NÃO TEM @")

# if not "#" in "dauster.pereira@ifb.edu.br":
#    print("NÃO TEM #")
# else:
#    print("TEM #")


#USANDO WHILE
# i = 0

# while i < 10:
#     print(f"Valor de i: {i}")
#     i += 1

# Solicitando que o usuário digite um valor

# i = 0
# while i < 10:
#     valor = int(input("Digite um valor:"))
#     print(f"Valor digitado: {valor}")
#     i += 1

#Só sairá do loop quando o usuário digitar 0

# valor = int(input("Digite um valor: "))
# while valor != 0:
#     print("Valor não aceito")
#     valor = int(input("Digite um valor: ")) 


#CORREÇÃO DE EXERCÍCIOS EM SALA (LAB) - Laços de Repetição

#Exercício 1
# for numero in range(0,11,2):
#    print(numero)

#Exercício 2
# for numero in range(51,101,2):
#    print(numero)

#Exercício 3
# for operador in range(1,11):
#     for operador_2 in range(1,11):
#         resultado = operador * operador_2
#         print(f"{operador} X {operador_2} = {resultado}")


#Exercício 4
# senha = input("Digite uma senha: ")

# while senha != "1234":
#     print("Senha incorreta!")
#     senha = input("Digite uma senha: ")

# print("Senha correta! Acesso permitido.")

#Exercício 5
# nota = float(input("Insira uma nota 0 até 10: "))

# while (nota < 0) or (nota > 10):
#     print("A nota não pode ser menor que 0 ou maior que 10!")
#     nota = float(input("Digite novamente outra nota:"))
# print("Nota válida")
