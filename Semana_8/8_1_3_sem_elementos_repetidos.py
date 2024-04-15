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
'''Os sets são uma coleção de itens desordenada, parcialmente imutável e que não podem 
conter elementos duplicados. Por ser parcialmente imutável, os sets possuem permissão 
de adição e remoção de elementos.

Além disso, os sets são utilizados, normalmente, com operações matemáticas de união, 
interseção e diferença simétrica.
Acesse o link: https://www.treinaweb.com.br/blog/manipulando-sets-no-python'''
conjunto = set(primeira + segunda)

# Converte o conjunto de volta para lista
lista_sem_repeticao = list(conjunto)

# Imprime a lista sem elementos repetidos
print(lista_sem_repeticao)