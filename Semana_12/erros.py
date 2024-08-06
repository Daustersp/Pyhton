# Tratamento de erros


import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# ERRO - DIVISÃO POR ZERO
# a = 1
# b = 0
# print(a/b)

# NOME CORRETO DO ARQUIVO
# with open ('Semana_12/arquivo.txt', 'r') as file_object:
#     texto = file_object.read()
#     print(texto)


# ERRO - NOME ERRADO DO ARQUIVO
# with open ('Semana_12/aruivo.txt', 'r') as file_object:
#     texto = file_object.read()
#     print(texto)


# USANDO O TRY
# try:
#     with open ('Semana_12/aruivo.txt', 'r') as file_object:
#         texto = file_object.read()
#         print(texto)
# except:
#     print('Deu ruim!!!')

# FileNotFoundError
# with open ('Semana_12/aruivo.txt', 'r') as file_object:
#     texto = file_object.read()
#     print(texto)

# FileNotFoundError -
# try:
#     with open ('Semana_12/aruivo.txt', 'r') as file_object:
#         texto = file_object.read()
#         print(texto)

# except:
#     print("Deu ruim")

# except FileNotFoundError as error:
#     print(error) # printando o erro FileNotFoundError


# FileNotFoundError - Erro genérico tem que ficar depois dos erros padrões
# try:
#     with open ('Semana_12/aruivo.txt', 'r') as file_object:
#         texto = file_object.read()
#         print(texto)

# except FileNotFoundError as error:
#     print(error) # printando o erro FileNotFoundError

# except:
#     print("Deu ruim")

# ZeroDivisionError
# a = 10
# b = 0
# print(a/b)

# ZeroDivisionError
# a = 10
# b = 0

# try:
#     print(a/b)

# except:
#     pass

# ZeroDivisionError
# a = 10
# b = 0

# try:
#     print(a/b)

# except ZeroDivisionError as error:
#     print(error)

# Else e Finally
# a = 10
# b = 2

# try:
#     print(a/b)

# except ZeroDivisionError as error:
#     print(error)

# else:
#     print('Sem erro')


# Else e Finally
# a = 10
# b = 2

# try:
#     print(a/b)

# except ZeroDivisionError as error:
#     print(error)

# else:
#     print('Sem erro')

# finally:
#     print('Aqui sempre vai printar')

# Else e Finally
a = 10
b = 0

try:
    print(a/b)

except ZeroDivisionError as error:
    print(error)

else:
    print('Sem erro')

finally:
    print('Aqui sempre vai printar')