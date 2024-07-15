from datetime import date

class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def __str__(self):
        status = "Emprestado" if self.emprestado else "Disponível"
        return f"Livro[ID={self.id}, Título={self.titulo}, Autor={self.autor}, Status={status}]"

class Pessoa:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f"Pessoa[ID={self.id}, Nome={self.nome}]"

class Emprestimo:
    def __init__(self, id, livro, pessoa, data_emprestimo, data_devolucao=None):
        self.id = id
        self.livro = livro
        self.pessoa = pessoa
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def registrar_devolucao(self, data_devolucao):
        self.data_devolucao = data_devolucao
        self.livro.emprestado = False

    def __str__(self):
        return (f"Empréstimo[ID={self.id}, Livro={self.livro.titulo}, Pessoa={self.pessoa.nome}, "
                f"Data de Empréstimo={self.data_emprestimo}, Data de Devolução={self.data_devolucao}]")

# Exemplo de utilização:
if __name__ == "__main__":
    # Criar instâncias de livros
    livro1 = Livro(1, "Python Programming", "Author A")
    livro2 = Livro(2, "Learning Java", "Author B")

    # Criar instância de pessoa
    pessoa1 = Pessoa(1, "João Silva")

    # Criar empréstimo
    emprestimo1 = Emprestimo(1, livro1, pessoa1, date(2024, 7, 9))
    livro1.emprestado = True

    print(livro1)
    print(pessoa1)
    print(emprestimo1)

    # Registrar devolução
    emprestimo1.registrar_devolucao(date(2024, 7, 19))
    print(emprestimo1)
    print(livro1)