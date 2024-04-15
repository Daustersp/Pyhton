import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

class Editora:
    def __init__(self, codigo, razao_social, contato, telefone):
        self.codigo = codigo
        self.razao_social = razao_social
        self.contato = contato
        self.telefone = telefone


class Livro:
    def __init__(self, codigo, descricao, isbn, editora):
        self.codigo = codigo
        self.descricao = descricao
        self.isbn = isbn
        self.editora = editora


# Criando objetos para a classe Editora
editora1 = Editora(1, "Editora A", "João", "123456789")
editora2 = Editora(2, "Editora B", "Maria", "987654321")

# Criando objetos para a classe Livro
livro1 = Livro(101, "Livro 1", "ISBN-1234", editora1)
livro2 = Livro(102, "Livro 2", "ISBN-5678", editora2)

# Exibindo informações dos objetos
print("Informações da Editora 1:")
print(f"Código: {editora1.codigo}")
print(f"Razão Social: {editora1.razao_social}")
print(f"Contato: {editora1.contato}")
print(f"Telefone: {editora1.telefone}")

print("\nInformações da Editora 2:")
print(f"Código: {editora2.codigo}")
print(f"Razão Social: {editora2.razao_social}")
print(f"Contato: {editora2.contato}")
print(f"Telefone: {editora2.telefone}")

print("\nInformações do Livro 1:")
print(f"Código: {livro1.codigo}")
print(f"Descrição: {livro1.descricao}")
print(f"ISBN: {livro1.isbn}")
print(f"Editora: {livro1.editora.razao_social}")

print("\nInformações do Livro 2:")
print(f"Código: {livro2.codigo}")
print(f"Descrição: {livro2.descricao}")
print(f"ISBN: {livro2.isbn}")
print(f"Editora: {livro2.editora.razao_social}")