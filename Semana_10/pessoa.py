# -----> SLIDE 6 e 7 <-----
# class Pessoa:
#     pass

# print(Pessoa) #Checar a classe

# pessoa1 = Pessoa() #Criando objeto a partir da classe (instância da classe)

# -----> SLIDE 8 e 9 <-----
# class Pessoa:
#     nome = "João"
#     idade = 30

# pessoa1 = Pessoa() #Criando objeto a partir da classe (instância da classe)
# print(pessoa1.nome) # Acessando o atributo nome - exibirá JOÃO

# pessoa1.nome = "Maria" #Alterando o atribudo nome
# print(pessoa1.nome) # Acessando o atributo nome - exibirá MARIA

# -----> SLIDE 11 e 12 <-----
# class Pessoa:
#     nome = "João"
#     idade = 30

#     def falar(self, mensagem):
#         print(f"{self.nome} diz: {mensagem}")

# pessoa1 = Pessoa() # Instanciando a classe
# pessoa1.nome = "Maria" #Se essa linha não for incluída, será exibido João
# pessoa1.falar("Olá") # A saída será: Maria diz: Olá

# -----> SLIDE 13 <----- CONSTRUTOR
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def falar(self, mensagem):
#         print(f"{self.nome} diz: {mensagem}")

# pessoa1 = Pessoa("João", 30) # Valores passados na instanciação da classe
# print(pessoa1.nome)
# print(pessoa1.idade)


# -----> SLIDE 19 <----- CARRO - ACELERAR
# class Carro:
#     def acelerar(self):
#         print("O carro está acelerando!")

# meu_carro = Carro()
# meu_carro.acelerar()

# -----> SLIDE 20 <----- CARRO - ACELERAR PASSANDO PARÂMETRO
class Carro:
    def acelerar(self, velocidade):
        print(f"O carro está acelerando a {velocidade} km/h!")

meu_carro = Carro()
meu_carro.acelerar(100)