import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

primeira = []
segunda = []
while True:
    e = int(input("Digite um valor para a primeira lista (0 para terminar): "))
    if e == 0:
        break
    primeira.append(e)

while True:
    e = int(input("Digite um valor para a segunda lista (0 para terminar): "))
    if e == 0:
        break
    segunda.append(e)

# Cria um conjunto com elementos das duas listas (elimina os repetidos)
conjunto = set(primeira + segunda)

# Converte o conjunto de volta para lista
lista_sem_repeticao = list(conjunto)

# Imprime a lista sem elementos repetidos
print(lista_sem_repeticao)