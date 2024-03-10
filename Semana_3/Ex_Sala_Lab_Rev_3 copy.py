# qtde_vendida = "TOP"
# print("A quantidade vendida foi "+ qtde_vendida)

# qtde_vendida = 1000
# print("A quantidade vendida foi "+ qtde_vendida)
import os
os.system("cls")

# if "dauster" in "dauster.pereira@ifb.edu.br":
#     print("TEM @")
# else:
#     print("NÃO TEM @")


# if not "ifb" in "dauster.pereira@ifb.edu.br":
#     print("NÃO TEM #")
# else:
#     print("TEM #")

# nome = input("Digite o seu nome: ")
# print("Nome", nome)
# pi=3.1415
# print(f'Valor de pi aproximado é {pi:.3f}')

# Prêmio da Mega-Sena
# total = float( input('Premio total da Mega: ') )

# # Número de ganhadores
# num = int( input('Numero de ganhadores: ') )

# print('Cada um vai ficar com R$ ', (total/num) )
#print('Cada um vai ficar com R$ %.2f' % (total/num) )



#Outro exemplo
# Prêmio da Mega-Sena
# total = float( input('Premio total da Mega: ') )

# # Número de ganhadores
# num = int( input('Numero de ganhadores: ') )

# print('O premio total foi R$%.2f para %d ganhadores, onde cada um ficou \
# com R$%.2f' %(total,num,total/num))

# #Usando a função round()
# num = 3.14159265359
# num_limitado = round (num, 2)
# print(num_limitado)


#Usando a formatação de string - usando formatação format()
# num = 3.14159265359
# num_limitado = "{:.2f}".format(num)
# print(num_limitado)

#Usando a formatação de string - usando operador de formatação de string f
# num = 3.14159265359
# num_limitado = f"{num:.2f}"
# print(num_limitado)

#Usando a f-string (só funciona nas versão do Python de 3 para cima ---3.1, 3.2, 3.3...)
qtde_vendida = 1500
custo_produto = 500
lucro = qtde_vendida - custo_produto
#print(f" O lucro foi de R${lucro}")

#print(f" O lucro foi de R${lucro}, a quantidade vendida foi de {qtde_vendida}")

#Como é feita a formatação usando o f-string --> variavel:,.2f
# , --> para utilizar o separador de milhar
# . --> para colocar o separador de decimal
# 2 --> para qtde de casas decimais
# f --> para dizer que é float

print(f" O lucro foi de R${lucro:,.2f}")


#CALCULAR MARGEM
margem = lucro / qtde_vendida
print(f"A margem foi de {margem:.2f}")

#CALCULAR MARGEM EM PERCENTAL
print(f"A margem foi de {margem:.2%}")


#COLOCAR NO FORMATO MOEDA BRASILEIRO
texto_lucro = f"R${lucro:,.2f}"
print(f"O lucro foi de {texto_lucro}")

#SUBSTITUIR A VÍRGULA POR UNDERLINE
texto_lucro = f"R${lucro:_.2f}"
print(f"O lucro foi de {texto_lucro}")

#UTILIZAR O .REPLACE PARA TROCAR
texto_lucro = f"R${lucro:_.2f}"
texto_lucro = texto_lucro.replace(".", ",").replace("_",".")
print(f"O lucro foi de {texto_lucro}")