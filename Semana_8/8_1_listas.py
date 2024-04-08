import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# LISTAS EM PYTHON
# lista1 = [1,2,3,4,5]
# lista2 = [6,7,8,9,10]
# lista3 = [11,12,13,14,15]
# todas_listas = [lista1,lista2,lista3]
# print(todas_listas)

# OUTRA FORMA DE DEFINIR LISTA
# lista1 = [
#             1,
#             2,
#             3,
#             4,
#             5
#         ]
# lista2 = [6,7,8,9,10]
# lista3 = [11,12,13,14,15]
# todas_listas = [lista1,lista2,lista3]
# print(todas_listas)

#ACESSANDO ITEM DA LISTA
# produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
# print(produtos[1])

# produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
# print(produtos[4])

# DUAS LISTAS DISTINTAS MAS QUE TÊM DADOS COMPLEMENTARES
# produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']

# vendas = [1000, 1500, 350, 270, 900]
# print('As vendas de {} foram de {}'.format(produtos[1],vendas[1]))


# DESCOBRIR O ÍNDICE DE UM ITEM CONHECIDO
# produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']

# i = produtos.index('mouse')
# print('O valor de i é '+str(i))
# print('O produto da posição i é '+str(produtos[i]))

# POSIÇÃO DE ITEM BASEADO NA INFORMAÇÃO DO USUÁRIO
# produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
# vendas = [1000, 1500, 350, 270, 900]

# produto = input('Insira o nome do produto em letra minúscula: ')
# i = produtos.index(produto)
# print(i)

# PRODUTO EM ESTOQUE
# produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
# estoque = [1000, 1500, 350, 270, 900]

# produto = input('Insira o nome do produto em letra minúscula: ')
# if produto in produtos:
#     i = produtos.index(produto)
#     qtde_estoque = estoque[i]
#     print('Temos {} unidade de {} no estoque'.format(qtde_estoque, produto))
# else:
#     print('{} não existe no estoque'.format(produto))


# ADICIONANDO PRODUTO EM ESTOQUE
# produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']

# produtos.append('iphone')
# print(produtos)

# REMOVENDO PRODUTO COM O REMOVE
# REMOVENDO PRODUTO COM O REMOVE
# produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']

# produtos.remove('mouse')
# print(produtos)

# REMOVENDO PRODUTO COM O POP
# produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet', 'geladeira', 'iphone']
# print(produtos)

# aux = produtos.pop(2)
# print(produtos)
# print(aux)

# USANDO O TRUY - verificando um produto que não existe na lista - ex: televisão
# produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
# item_usuario = input('Qual item deseja remover? ')

# try:
#     produtos.remove(item_usuario)
#     print(produtos)
# except:
#     print('O produto {} não existe na lista. '.format(item_usuario))

# USANDO O TRUY - verificando um produto que existe na lista - ex: tablet
# produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
# item_usuario = input('Qual item deseja remover? ')

# try:
#     produtos.remove(item_usuario)
#     print(produtos)
# except:
#     print('O produto {} não existe na lista. '.format(item_usuario))

# 3 MÉTODOS PARA LISTA
# vendas = [10,50,670,16,46,87,99]
# print(len(vendas))
# print(max(vendas))
# print(min(vendas))

# JUNTAR LISTAS COM O EXTENDE
# produtos = ['apple tv','mac','iphone x', 'Ipad', 'apple watch', 'macbook', 'airpods']
# novos_produtos = ['chromecast', 'windows', 'windows phone']

# produtos.extend(novos_produtos)
# print(produtos)

# JUNTAR LISTAS COM O SINAL DE +
# produtos = ['apple tv','mac','iphone x', 'Ipad', 'apple watch', 'macbook', 'airpods']
# novos_produtos = ['chromecast', 'windows', 'windows phone']

# produtos_compilado = produtos + novos_produtos
# print(produtos_compilado)

# JUNTAR LISTAS COM O APPEND E COM O SINAL DE +
# produtos = ['apple tv','mac','iphone x', 'Ipad', 'apple watch', 'macbook', 'airpods']
# novos_produtos = ['chromecast', 'windows', 'windows phone']

# print('Usando o +: ')
# produtos_compilado = produtos + novos_produtos
# print(produtos_compilado)

# print('Usando o Append: ')
# produtos.append(novos_produtos)
# print(produtos)

# SE TIVER ITENS IGUAIS NA LISTA ORIGINAL
# produtos = ['apple tv','mac','iphone x', 'Ipad', 'airpods']
# novos_produtos = ['chromecast', 'airpods']

# produtos.extend(novos_produtos)
# print(produtos)

# ORDENANDO LISTAS COM O SORT()
# produtos = ['apple tv','mac','iphone x', 'Ipad', 'airpods']
# vendas = [1000, 1500, 15000, 270, 900]

# #Ordenando a lista de produtos
# produtos.sort()
# print(produtos)

# ORDENANDO LISTAS NUMÉRICAS COM O SORT()
produtos = ['apple tv','mac','iphone x', 'Ipad', 'airpods']
vendas = [1000, 1500, 15000, 270, 900]

#Ordenando a lista de produtos
vendas.sort()
print(vendas)