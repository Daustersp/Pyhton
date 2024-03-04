import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

#ORDEM DECRESCENTE
primeiro = int(input('Digite o primeiro número: '))
segundo  = int(input('Digite o segundo número : '))
terceiro = int(input('Digite o terceiro número: '))
print(primeiro,'-',segundo,'-',terceiro)

if(segundo < primeiro):
    aux = primeiro
    primeiro = segundo
    segundo = aux

if(terceiro < primeiro):
    aux = primeiro
    primeiro = terceiro
    terceiro = aux

if(terceiro < segundo):
    aux = segundo
    segundo = terceiro
    terceiro = aux

print(primeiro,'-',segundo,'-',terceiro)



#ORDEM CRESCENTE
# primeiro = int(input('Digite o primeiro número: '))
# segundo  = int(input('Digite o segundo número : '))
# terceiro = int(input('Digite o terceiro número: '))
# print(primeiro,'-',segundo,'-',terceiro)

# if(terceiro > segundo):
#     aux = terceiro
#     terceiro = segundo
#     segundo = aux

# if(segundo > primeiro):
#     aux = segundo
#     segundo = primeiro
#     primeiro = aux

# if(terceiro > segundo):
#     aux = terceiro
#     terceiro = segundo
#     segundo = aux

# print(primeiro,'-',segundo,'-',terceiro)