import random

palavras = ["python", "programacao", "computador", "linguagem", "tecnologia"]

palavra_secreta = random.choice(palavras)

letras_adivinhadas = []

forca = [
    "   _ _ _",
    "  |      |",
    "  |      O",
    "  |     /|\\",
    "  |     / \\",
    " _|_"
]

tentativas_max = len(forca)


def exibir_forca(erros):
    for i in range(erros):
        print(forca[i])


def exibir_progresso(palavra, letras_adivinhadas):
    resultado = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado


erros = 0
while erros < tentativas_max:
    letra = input("Adivinhe uma letra: ").lower()

    if letra in palavra_secreta:
        letras_adivinhadas.append(letra)
        print("Letra correta!")
    else:
        erros += 1
        print("Letra errada. Você tem {} tentativas restantes.".format(tentativas_max - erros))

    progresso = exibir_progresso(palavra_secreta, letras_adivinhadas)
    print(progresso)

    exibir_forca(erros)

    if progresso == palavra_secreta:
        print("Parabéns! Você ganhou. A palavra era: " + palavra_secreta)
        break

if erros == tentativas_max:
    print("Você perdeu. A palavra era: " + palavra_secreta)