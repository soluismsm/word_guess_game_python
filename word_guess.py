from os import system
from random import sample

"""
! Não usar requests pois deixa pesado
TODO: Guardar a lista de palavras num arquivo.txt
TODO: Adicionar um loop caso o usuário queira jogar de novo
TODO: Adicionar sistema de Pontos
TODO: Adicionar sistema de dificuldade por palavras
TODO: Adicionar tentativas finitas
TODO: Adicionar comentários
"""


def verify_user_input(user_input):
    if user_input.isalpha() and len(user_input) == 1 or user_input == "":
        return True


def choose_random_word(palavras_lista):
    while True:
        palavra = sample(palavras_lista)
        return palavra


def print_formatted_word(palavra_formada):
    print(f"Palavra formatada: {''.join(palavra_formada)}\n")


def lista_secreta():
    palavras_secretas = (
        "acabar",
        "brinquedo",
        "cama",
        "delegado",
        "esporte",
        "faminto",
        "grupo",
        "hiena",
        "inteligente",
        "jogo",
        "ketchup",
        "luz",
        "macaco",
        "natureza",
        "orgulhoso",
        "parque",
        "quiosque",
        "rinoceronte",
        "sucata",
        "telefone",
        "ultrapassar",
        "vidro",
        "website",
        "xadrez",
        "yoga",
        "zangado",
    )
    return palavras_secretas


def jogar_forca():
    palavras_secretas = lista_secreta()
    palavra_secreta = choose_random_word(palavras_secretas)
    palavra_formada = ["_"] * len(palavra_secreta)
    user_tries = 0
    user_guesses = []

    while "_" in palavra_formada:
        user_input = input("Digite uma letra: ")
        if not verify_user_input(user_input):
            print("Entrada inválida. Digite uma letra.")
            continue

        found_letters = 0
        if user_input not in user_guesses:
            for i, letra in enumerate(palavra_secreta):
                if user_input == letra:
                    palavra_formada[i] = user_input
                    found_letters += 1
            print(f"Você encontrou {found_letters} letra(s)")
        else:
            print(f"A letra '{user_input}' já foi usada. Tente outra")

        user_tries += 1
        user_guesses.append(user_input)
        print_formatted_word(palavra_formada)

    system("cls")
    print(f"A palavra é {''.join(palavra_formada)}")
    print(f"Parabéns você adivinhou a palavra em {user_tries} tentativas")


jogar_forca()
