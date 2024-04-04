import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# CLASSE PARA CLIENTES DE UM BANCO (SLIDE 40)
# 1, 2, 3	
# class Cliente:
# 	def __init__(self, nome, codigo):
# 		self.nome = nome
# 		self.codigo = codigo
		
# 4, 5	
# class CartaoDeCredito:
# 	def __init__(self, num_cartao, data_validade):
# 		self.num_cartao = num_cartao
# 		self.data_validade = data_validade

# 6, 7			
# class Agencia:
# 	def __init__(self, num_agencia):
# 		self.num_agencia = num_agencia

# 8, 9			
# class Conta:
# 	def __init__(self, num_conta, saldo, limite):
# 		self.num_conta = num_conta
# 		self.saldo = saldo
# 		self.limite = limite

# 10			
class Conta:
	def __init__(self, num_conta, saldo):
		self.num_conta = num_conta
		self.saldo = saldo
		self.limite = "100"

# 1, 2, 3				
# cliente1 = Cliente("Dauster", "1050")
# cliente2 = Cliente("Júlia", "2002")
# cliente3 = Cliente("Priscilla", "3303")
# print(cliente1.nome, cliente1.codigo)
# print(cliente2.nome, cliente2.codigo)
# print(cliente3.nome, cliente3.codigo)
# print(f"O nome do primeiro objeto é {cliente1.nome} e seu código é {cliente1.codigo}")

# 4, 5			
# cartaodecredito1 = CartaoDeCredito("5100.0101.0202.9393", "03/2030")
# cartaodecredito2 = CartaoDeCredito("6100.0202.0202.2222", "03/2027")
# print(cartaodecredito1.num_cartao, cartaodecredito1.data_validade)
# print(cartaodecredito2.num_cartao, cartaodecredito2.data_validade)

# 6, 7	
# agencia1 = Agencia("001")
# agencia2 = Agencia("002")
# print(agencia1.num_agencia)
# print(agencia2.num_agencia)

# 8, 9	
# conta1 = Conta("001", "2000","7000")
# conta2 = Conta("002", "1000","5000")
# print(conta1.num_conta, conta1.saldo, conta1.limite)
# print(conta2.num_conta, conta2.saldo, conta2.limite)

# 10
conta1 = Conta("001", "2000")
conta2 = Conta("002", "1000")
print(conta1.num_conta, conta1.saldo, conta1.limite)
print(conta2.num_conta, conta2.saldo, conta2.limite)