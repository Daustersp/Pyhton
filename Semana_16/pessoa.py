import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        """Aumenta a idade da pessoa e, se a idade for menor que 21 anos, aumenta a altura em 0,5 cm."""
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5

    def engordar(self, quilos):
        """Aumenta o peso da pessoa em um valor especificado."""
        self.peso += quilos

    def emagrecer(self, quilos):
        """Diminui o peso da pessoa em um valor especificado."""
        self.peso -= quilos

    def crescer(self, centimetros):
        """Aumenta a altura da pessoa em um valor especificado."""
        self.altura += centimetros

    def mostrar_informacoes(self):
        """Exibe as informações atuais da pessoa."""
        return f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso:.2f} kg, Altura: {self.altura:.2f} cm"

# Criando uma instância da classe Pessoa
pessoa = Pessoa(nome="João", idade=20, peso=70, altura=175)

# Mostrando informações iniciais
print("Informações iniciais:")
print(pessoa.mostrar_informacoes())

# Envelhecer a pessoa
pessoa.envelhecer()
print("\nApós envelhecer 1 ano:")
print(pessoa.mostrar_informacoes())

# Engordar a pessoa
pessoa.engordar(5)
print("\nApós engordar 5 kg:")
print(pessoa.mostrar_informacoes())

# Emagrecer a pessoa
pessoa.emagrecer(3)
print("\nApós emagrecer 3 kg:")
print(pessoa.mostrar_informacoes())

# Crescer a pessoa
pessoa.crescer(2)
print("\nApós crescer 2 cm:")
print(pessoa.mostrar_informacoes())