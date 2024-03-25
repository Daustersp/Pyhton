# A estrutura básica da Python range é:

# range([start], [stop], [step])

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

#CRIAÇÃO DE CLASSE
# class ControleRemoto:
#     def __init__(self):
#         cor = ""
#         altura = ""
#         profundidade = ""
#         largura = ""


#CRIAÇÃO DE CLASSE
# class ControleRemoto:
#     def __init__(self, cor, altura, profundidade, largura):
#         cor = "preto"
#         altura = "10cm"
#         profundidade = "2cm"
#         largura = "2cm"


#CRIAÇÃO DE CLASSE - 2 CONTROLES DIFERETNES
# class ControleRemoto:
#     def __init__(self, cor, altura, profundidade, largura):
#         cor = "preto"
#         altura = "10cm"
#         profundidade = "2cm"
#         largura = "2cm"

# controle_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm")
# controle_remoto2 = ControleRemoto("cinza", "10cm", "2cm", "2cm")


# PERSONARLIZAR ALTERANDO PARÂMETROS
# class ControleRemoto:
#     def __init__(self, cor, altura, profundidade, largura):
#         self.cor = cor
#         self.altura = altura
#         self.profundidade = profundidade
#         self.largura = largura

# USANDO O PRINT PARA RETORNAR
# class ControleRemoto:
#     def __init__(self, cor, altura, profundidade, largura):
#         self.cor = cor
#         self.altura = altura
#         self.profundidade = profundidade
#         self.largura = largura

# controle_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm")
# controle_remoto2 = ControleRemoto("cinza", "10cm", "2cm", "2cm")

# print(controle_remoto.cor)
# print(controle_remoto.altura)


# CLASSE PARA CLIENTES DA NETFLIX
# vamos criar uma classe para Clientes da Netflix
class Cliente:
	def __init__(self, nome, email, plano):
		self.nome = nome
		self.email = email
		lista_planos = ["basic", "premium"]
		if plano in lista_planos:
			self.plano = plano
		else:
			raise Exception("Plano inválido")


cliente = Cliente("Dauster", "daustersp@gmail.com", "blabla")
print(cliente.nome)
