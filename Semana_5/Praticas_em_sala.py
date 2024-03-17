# A estrutura básica da Python range é:

# range([start], [stop], [step])

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# A Estrutura da lista é essa:
# nome_da_lista = ["ITEM 1", "ITEM 2", "ITEM 3"]

# Imprimindo listas
# listas1 = [1,2,3,4,5]
# listas2 = [6,7,8,9,10]
# listas3 = [11,12,13,14,15]
# todas_listas = [listas1,listas2,listas3]
# print(todas_listas)

# Outra forma de definir a lista
# nome_da_lista = [
#     "ITEM 1",
#     "ITEM 2",
#     "ITEM 3"
#     ]


# Listas
# produtos = ["tv", "celular", "mouse", "teclado", "tablet"]
# print(produtos[1])

# produtos = ["tv", "celular", "mouse", "teclado", "tablet"]
# print(produtos[4])

# vendas = [1000, 1500, 350, 270, 900]
# print("As vendas de {} foram de {}".findformat(produtos[1], vendas[1]))

# Acessar a lista por seus índices
# produtos = ["tv", "celular", "mouse", "teclado", "tablet"]

# i = produtos.index("mouse")
# print("O valor de i é "+ str(i))
# print("O produto da posição i é "+str(produtos[i]))

# Se um item que estou buscando não está na lista?
# Como chegar essa informação?
# produtos = ["tv", "celular", "tablet", "teclado", "geladeira", "forno"]
# estoque = [100, 150, 100, 120, 70, 180, 80]

# produto = input("Insira o nome do produtp em letra minúscula: ")
# i = produtos.index(produto)
# print(i)

# Como resolver o problema do item que não está na lista
# produtos = ["tv", "celular", "tablet", "teclado", "geladeira", "forno"]
# estoque = [100, 150, 100, 120, 70, 180, 80]

# produto = input("Insira o nome do produtp em letra minúscula: ")
# if produto in produtos:
#     i = produtos.index(produto)
#     qtde_estoque = estoque[1]
#     print("Temos {} unidade de {} no estoque".format(qtde_estoque, produto))
# else:
#     print("O item {} não existe no estoque".format(produto))


# Adicionando um item a lista usando APPEND
# produtos = ["tv", "celular", "tablet", "teclado", "geladeira", "forno"]
# produtos.append("iphone")
# print(produtos)    

# Removendo um item a lista usando POP
# POP - retira o valor da lista, mas não o DELETA
# O POP utiliza-se do índice para a remoção
produtos = ["tv", "celular", "tablet", "teclado", "geladeira", "forno"]
print(produtos)
print()
aux = produtos.pop(2)
print(produtos)    
print(aux)

# Removendo um item a lista usando REMOVE
# REMOVE - DELETA o valor da lista
# O remove não utiliza do índice para a remoção
produtos = ["tv", "celular", "tablet", "teclado", "geladeira", "forno"]
print(produtos)
print()
produtos.remove("tablet")
print(produtos)