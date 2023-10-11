#calculo===================
def soma (n1, n2):
    resultado = n1 + n2
    print(resultado)


def sub (n3, n4):
    resultado = n3 - n4
    print(resultado)


def mult (n5, n6):
    resultado = n5 * n6
    print(resultado)



def divi (n7, n8):
    resultado = n7 / n8
    print(resultado)

#piramede===============================

def piramede (numb):
    for x in range (1, numb + 1):
        for y in range (1 , x + 1):
            print(y, end = " ")
        print( )

#vogais=================================

def totalvog(texto):
    cont = 0
    for x in texto:
        if x in "aeiouAEIOU":
            cont += 1
    print(f"O total de vogais é {cont}.")


def estoque1(produto, quantidade, valor):
    vTotal = quantidade * valor
    return vTotal


def vog(texto):
    cont = 0
    for x in texto:
        if x in "aeiouAEIOU":
            cont += 1
    print(f"{cont}")

#estoque========================================

def estoque (produto, quant, valor_unit):
    total_estoque = quant * valor_unit
    return produto, total_estoque

#analise========================================

def analise(numero):
    if numero > 0:
        return "P"
    elif numero < 0:
        return "N"
    elif numero == 0:
        return "Z"
    else:
        print("Burro")

#Numeros indefinidos==================================

def adicao(*param):
    result = 0
    for x in param:
        result += x
    return result

#total letraas========================================

def totalletras(texto):
    cont = 0
    for x in texto:
        if x in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVxXzZ ":
            cont += 1
    print(cont)

    for x in range(len(texto)-1, -1 , -1):
        print(texto[x], end="")

#lista repetiçao===========================================

def repeticao(list):
    list2 = []
    for x in list:
        if x not in list2:
            list2.append(x)
    print(list2)
