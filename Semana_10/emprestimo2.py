import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

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


#executa as instruções do empréstimo
lista_livro = []
id = 0
instrucao = 0
while instrucao != 4:
        
    instrucao = int(input("Digite o número da opção: 1 - adicionar livro, 2 - realizar emprestimo, 3 - excluir, 4 - imprimir ou 5 - sair: \n"))
    
    #adiciona dados dos livros
    if instrucao == 1: 
        # Criar instâncias de livros
        titulo = input("Título do Livro: \n")
        autor = input("Autor do Livro: \n")
        id = id + 1
        livro = Livro(id, titulo, autor)
        lista_livro.append(livro)
        print("\nSeu livro foi inserido \n")

    #exclui dados da agenda, mas mantém agenda
    elif instrucao == 3:
        while True:
            contador = 0
            for livro in lista_emprestimo:
                print(f"{livro.titulo_livro, livro.autor_livro} - {contador}")
                contador += 1
            print(f"\nSe desistiu, digite {contador} para sair!\n")
            contador_selecionado = input("\n Qual o número da informação deseja excluir?\n")
            if contador_selecionado.isnumeric():
                contador_novo = int(contador_selecionado)
                if contador_novo in range(0, contador):
                    print("\nEstamos excluindo... quase lá...\n")
                    lista_selecionada = lista_emprestimo.pop(contador_novo) #Apaga o item
                    print(f"\nO livro {lista_selecionada.titulo_livro, lista_selecionada.autor_livro} foi excluído!\n") #Item foi excluído
                    break #Sai do loop
                elif contador_novo == contador:
                    break   #Sai do loop
                else:
                    print("Informação não existe.")
            else:
                print("Informação incorreta.")
    
    #imprime acervo da biblbioteca
    elif instrucao == 4:
        for acervo in lista_livro:
            print(f"\nAcervo da biblioteca: {acervo.titulo, acervo.autor, acervo.emprestado}\n")

    #sai da agenda
    elif instrucao == 5:
        print(f'\n<< Empréstimos realizados! >>')
        break
    #caso usuário digite opção inexistente
    elif instrucao >=6: 
        print("Essa opção não existe!")