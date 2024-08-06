
import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# # Solicita dois números ao usuário
# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
    
# # Soma os números
# soma = num1 + num2
    
# # Mostra o resultado
# print(f"A soma de {num1} e {num2} é {soma}.")
    





#USANDO O TRATAMENTO DE EXCEÇÃO
# try:
#     # Solicita dois números ao usuário
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
    
#     # Soma os números
#     soma = num1 + num2
    
#     # Mostra o resultado
#     print(f"A soma de {num1} e {num2} é {soma}.")
    
# except ValueError:
#     # Captura erros de valor não numérico e exibe uma mensagem simpática
#     print("Oops! Parece que você não digitou um número válido. Por favor, tente novamente.")


#USANDO FUNÇÃO - TRATAMENTO DE EXCEÇÃO
def somar(a, b):
    try:
        resultado = float(a) + float(b)
        return resultado
    except ValueError:
        return "Oops! Parece que você não digitou um número válido. Por favor, tente novamente."

# Exemplo de uso:
a = input("Digite o primeiro número: ")
b = input("Digite o segundo número: ")

resultado = somar(a, b)
print("Resultado:", resultado)