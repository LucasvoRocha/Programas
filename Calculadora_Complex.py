from biblioteca import *
while True:
    opera = input("Escolha uma operação: 1 somar, 2 subtrair, 3 multiplicar, 4 dividir ou S para sair: ")
    if opera not in "s":

        n1 = float(input("Digite um numero: "))
        n2 = float(input("Digite outro numero: "))

    if opera == "1":
        soma (n1, n2)

    elif opera == "2":
        sub (n1, n2)

    elif opera == "3":
        mult (n1, n2)

    elif opera == "4":
        divi (n1, n2)

    elif opera in "s":
        break

    else:
        print("Digite uma operação valida. ")]
