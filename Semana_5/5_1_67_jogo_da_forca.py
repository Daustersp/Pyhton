# A estrutura básica da Python range é:

# range([start], [stop], [step])

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "algoritmo", "desenvolvimento"]
    return random.choice(palavras)

def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra secreta tem", len(palavra_secreta), "letras.")

    while True:
        palavra_atual = ""
        for letra in palavra_secreta:
            if letra in letras_corretas:
                palavra_atual += letra
            else:
                palavra_atual += "_"

        print("\nPalavra:", palavra_atual)
        print("Tentativas restantes:", tentativas)

        if palavra_atual == palavra_secreta:
            print("Parabéns! Você ganhou!")
            break

        if tentativas == 0:
            print("Você perdeu! A palavra secreta era:", palavra_secreta)
            break

        palpite = input("Digite uma letra: ").lower()

        if palpite in letras_corretas:
            print("Você já tentou essa letra.")
        elif palpite in palavra_secreta:
            print("Correto! A letra", palpite, "está na palavra.")
            letras_corretas.append(palpite)
        else:
            print("Incorreto! A letra", palpite, "não está na palavra.")
            tentativas -= 1

jogar_forca()