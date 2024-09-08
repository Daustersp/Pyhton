import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

#SOLUÇÃO USANDO LISTAS
res = []
res.append(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
res.append(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
res.append(input("Devia para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))

soma_respostas = 0
for i in res: # soma o número de respostas
    soma_respostas += int(i)

if (soma_respostas < 2):
    print("\nInocente")
elif (soma_respostas == 2):
    print("\nSuspeita")
elif (3 <= soma_respostas <= 4):
    print("\nCúmplice")
elif (soma_respostas == 5):
    print("\nAssassino")


# SOLUÇÃO SEM USAR LISTAS
# lista_perguntas = ["Telefonou para a vítima? 1/Sim ou 0/Não: ",
#                 "Esteve no local do crime? 1/Sim ou 0/Não: ",
#                 "Mora perto da vítima? 1/Sim ou 0/Não: ",
#                 "Devia para a vítima? 1/Sim ou 0/Não: ",
#                 "Já trabalhou com a vítima? 1/Sim ou 0/Não: "]

# res = []
# soma_respostas = 0
# for i in range(len(lista_perguntas)):
#     print(lista_perguntas[i])
#     res.append(input()) # adiciona as respostas na lista res
#     soma_respostas += int(res[i]) # soma o número de respostas

# status = ["Inocente","Suspeita","Cúmplice","Cúmplice","Assassino"]
# if soma_respostas < 2:
#     print(status[0])
# else:
#     print(status[soma_respostas-1])
