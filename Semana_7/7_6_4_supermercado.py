import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque


class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Pedido:
    def __init__(self, itens, forma_pagamento):
        self.itens = itens
        self.forma_pagamento = forma_pagamento


# Criando objetos para a classe Produto
produto1 = Produto("Arroz", 5.99, 100)
produto2 = Produto("Feijão", 7.99, 80)

# Criando objetos para a classe ItemPedido
item1 = ItemPedido(produto1, 2)
item2 = ItemPedido(produto2, 3)

# Criando objeto para a classe Pedido
pedido1 = Pedido(item1, "cartão")
pedido2 = Pedido(item2, "dinheiro")

# Exibir na tela
print(f"Produto: {item1.produto.nome}, Quantidade: {item1.quantidade}, Forma de pagamento: {pedido1.forma_pagamento}")
print(f"Produto: {item2.produto.nome}, Quantidade: {item2.quantidade}, Forma de pagamento: {pedido2.forma_pagamento}")