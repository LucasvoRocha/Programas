import random

def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]

    while True:
        escolha_jogador = input("Escolha pedra, papel ou tesoura: ").lower()
        escolha_computador = random.choice(opcoes)

        print(f"Você escolheu: {escolha_jogador}")
        print(f"O computador escolheu: {escolha_computador}")

        if escolha_jogador in opcoes:
            if escolha_jogador == escolha_computador:
                print("Empate!")
            elif (
                (escolha_jogador == "pedra" and escolha_computador == "tesoura")
                or (escolha_jogador == "papel" and escolha_computador == "pedra")
                or (escolha_jogador == "tesoura" and escolha_computador == "papel")
            ):
                print("Você ganhou!")
            else:
                print("O computador ganhou!")
        else:
            print("Escolha inválida. Por favor, escolha pedra, papel ou tesoura.")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != "s":
            break

print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")
jogar_jokenpo()
