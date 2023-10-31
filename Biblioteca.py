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

#Conta bancaria============================================

class contabancaria:
    def __init__(self, numero, saldo, nome, tipo, limite):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = "inativa"
        self.limite = limite

    def ativar_conta(self):
        self.status = "ativa"

    def desativar_conta(self):
        self.status = "inativa"

    def depositar(self, valor):
        if self.status == "ativa" and valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}"
        else:
            return "Não é possível realizar o depósito."

    def sacar(self, valor):
        if self.status == "ativa" and 0 < valor <= (self.saldo + self.limite):
            self.saldo -= valor
            return f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}"
        else:
            return "Não é possível realizar o saque."

    def verificar_saldo(self):
        if self.status == "ativa":
            return f"Saldo disponível: R${self.saldo}"
        else:
            return "Conta inativa. Não é possível verificar o saldo."

#animal==================================

class animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer...")

    def emitir_som(self):
        print(f"O {self.nome} esta emitindo som...")
#subclasse
class gato(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class vaca(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class boi(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class cachorro(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class galinha(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class masqueico(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
