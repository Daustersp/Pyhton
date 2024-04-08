import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# class ControleRemoto:
#     def __init__(self, cor, altura, profundidade, largura):
#         self.cor = cor
#         self.altura = altura
#         self.profundidade = profundidade
#         self.largura = largura
















#CRIAÇÃO DE CLASSE
# class ControleRemoto:
#     def __init__(self):
#         cor = ""
#         altura = ""
#         profundidade = ""
#         largura = ""


#CRIAÇÃO DE CLASSE - adicionar elementos da inicialização
# class ControleRemoto:
#     def __init__(self, cor, altura, profundidade, largura):
#         cor = "preto"
#         altura = "10cm"
#         profundidade = "2cm"
#         largura = "2cm"


#CRIAÇÃO DE CLASSE - 2 CONTROLES DIFERETNES (Slide 31)
# class ControleRemoto:
#     def __init__(self, cor, altura, profundidade, largura):
#         cor = "preto"
#         altura = "10cm"
#         profundidade = "2cm"
#         largura = "2cm"

# controle_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm")
# controle_remoto2 = ControleRemoto("cinza", "10cm", "2cm", "2cm")


# PERSONARLIZAR ALTERANDO PARÂMETROS (SLIDE 32)
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



# EM SALA (SLIDE 35)
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



# CLASSE PARA CLIENTES DA NETFLIX (SLIDE 38)
# class Cliente:
# 	def __init__(self, nome, email, plano):
# 		self.nome = nome
# 		self.email = email
# 		lista_planos = ["basic", "premium"]
# 		if plano in lista_planos:
# 			self.plano = plano
# 		else:
# 			raise Exception("Plano inválido")

# cliente = Cliente("Dauster", "daustersp@gmail.com", "blabla")
# print(cliente.nome)


#importando o tkinter
from tkinter import *
janela = Tk()
janela.title("Olá Mundo")
janela.mainloop()