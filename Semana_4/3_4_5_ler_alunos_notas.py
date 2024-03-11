# A estrutura básica da Python range é:

# range([start], [stop], [step])

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

qtde_alunos = int(input("Quantos alunos existem na turma: "))
soma = 0
for i in range(qtde_alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    soma = soma + nota

media = float(soma / qtde_alunos)

print(f"A média aritmética das notas dos alunos é: {media:.1f}")
