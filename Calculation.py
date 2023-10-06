while True:
    n1 = float(input("Digite um numero: "))
    opera = input("Escolha uma operação: +, -, /, x. ")
    n2 = float(input("Digite outro numero: "))

    if opera == "+":
        soma = n1 + n2
        print(f"O resultado da sua soma é {soma}")
    elif opera == "-":
        sub = n1 - n2
        print(f"O resultado da sua subtração é {sub}")
    elif opera == "/":
        if n2 == 0:
            print(f"nenhum numero divisivel por {n2}")
        else:
            divi = n1 / n2
            print(f"O resultado da sua divisão é {divi}")
    elif opera == "x":
        multi = n1 * n2
        print(f"O resultado da sua multiplicação é {multi}")
    else:
        print("TU É BURRO É")
