def piramede (numb):
    for x in range (1, numb + 1):
        for y in range (1 , x + 1):
            print(y, end = " ")
        print( )



from gizebibli2 import *
numb = int(input("Digite um número: "))
piramede(numb)
