import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Função para obter o nome do mês por extenso
def nome_mes(mes):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    return meses[mes - 1]

# Recebe as temperaturas médias de cada mês
temperaturas = []
for i in range(1, 13):
    temperatura = float(input(f"Digite a temperatura média do mês {nome_mes(i)}: "))
    temperaturas.append(temperatura)

# Calcula a média anual das temperaturas
media_anual = sum(temperaturas) / len(temperaturas)

# Encontra as temperaturas acima da média anual e seus respectivos meses
acima_da_media = []
for i, temperatura in enumerate(temperaturas):
    if temperatura > media_anual:
        acima_da_media.append((i + 1, nome_mes(i + 1), temperatura))

# Mostra a média anual e as temperaturas acima da média com os meses correspondentes
print(f"Média anual das temperaturas: {media_anual:.2f} °C")
print("Temperaturas acima da média anual:")
for mes_numero, mes_nome, temperatura in acima_da_media:
    print(f"{mes_numero} - {mes_nome}: {temperatura} °C")