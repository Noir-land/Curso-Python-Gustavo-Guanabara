"""
Crie um algoritmo que leia um número e 
mostre o seu dobro, o seu triplo e sua raiz quadrada
"""

n = int(input("Digite um numero: "))
print("O dobro de {} é {}".format(n, n*2), end=". ")
print("O triplo de {} é {}".format(n, n*3), end=" e ")
print("A raiz quadrada de {} é {}".format(n, n**(1/2)))
