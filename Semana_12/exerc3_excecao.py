
import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração


try:
    with open ('Semana_12/cats.txt', 'r') as file_object:
        texto = file_object.read()
        print("Esses são meus gatos!!!")
        print(texto)
        print("\n")

except FileNotFoundError as error:
    print(f"Oops! O arquivo cats.txt não foi encontrado. Por favor, verifique se o nome está correto e se o arquivo está no diretório certo.") # printando o erro FileNotFoundError
    print("\n")


try:
    with open ('Semana_12/dogs.txt', 'r') as file_object:
        texto = file_object.read()
        print("Esses são meus cachorros!!!")
        print(texto)
        print("\n")

except FileNotFoundError as error:
    print(print(f"Oops! O arquivo dogs.txt não foi encontrado. Por favor, verifique se o nome está correto e se o arquivo está no diretório certo.")) # printando o erro FileNotFoundError
    print("\n")




## OU
# Lista de arquivos a serem lidos
# arquivos = ['Semana_12/cats.txt', 'Semana_12/dogs.txt']

# # Loop sobre cada arquivo na lista
# for arquivo in arquivos:
#     try:
#         # Tenta abrir e ler o arquivo
#         with open(arquivo, 'r') as file:
#             conteudo = file.read()
#             print(f"Conteúdo de {arquivo}:")
#             print(conteudo)
#             print()  # Linha em branco para separar o conteúdo dos arquivos
#     except FileNotFoundError:
#         # Captura o erro de arquivo não encontrado e exibe uma mensagem simpática
#         print(f"Oops! O arquivo {arquivo} não foi encontrado. Por favor, verifique se o nome está correto e se o arquivo está no diretório certo.")