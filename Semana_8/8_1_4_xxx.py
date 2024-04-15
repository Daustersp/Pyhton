import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Função para obter o nome do mês por extenso
# def nome_mes(mes):
#     meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
#     return meses[mes - 1]

# Recebe as temperaturas médias de cada mês
# temperaturas = []
# for i in range(1, 13):
#     temperatura = float(input(f"Digite a temperatura média do mês {nome_mes(i)}: "))
#     temperaturas.append(temperatura)

# Calcula a média anual das temperaturas
# media_anual = sum(temperaturas) / len(temperaturas)

# Encontra as temperaturas acima da média anual e seus respectivos meses
# acima_da_media = []
# for i, temperatura in enumerate(temperaturas):
#     if temperatura > media_anual:
#         acima_da_media.append((i + 1, nome_mes(i + 1), temperatura))

# # Mostra a média anual e as temperaturas acima da média com os meses correspondentes
# print(f"Média anual das temperaturas: {media_anual:.2f} °C")
# print("Temperaturas acima da média anual:")
# for mes_numero, mes_nome, temperatura in acima_da_media:
#     print(f"{mes_numero} - {mes_nome}: {temperatura} °C")




# class Produto:
#     def __init__(self, nome, preco, estoque):
#         self.nome = nome
#         self.preco = preco
#         self.estoque = estoque

# class ItemPedido:
#     def __init__(self, produto, quantidade):
#         self.produto = produto
#         self.quantidade = quantidade

# class Pedido:
#     def __init__(self, itens, qtde_pedido, tipo_pagto):
#         self.itens = itens
#         self.qtde = qtde_pedido
#         self.tipo_pagto = tipo_pagto

# produto1 = Produto("arroz", "100", "200")
# produto2 = Produto("milho", "50", "20")

# item_pedido1 = ItemPedido("arroz", "10")
# item_pedido2 = ItemPedido("milho", "5")

# pedido1 = Pedido("arroz", "2", "Dinheiro")
# pedido2 = Pedido("milho", "2", "Cheque")

# print(produto1.nome)
# print(item_pedido1.quantidade)
# print(pedido2.tipo_pagto)
