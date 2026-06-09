"""
Crie um programa que leia um número real qualquer 
pelo teclado e mostre na tela a sua porção inteira.
"""

from math import floor
n = float(input("Digite um numero: "))
print("O valor digitado foi {} e seu numero inteiro é {}".format(n, floor(n)))
# n = float(input("Digite um numero: "))
# print("O valor é {} e sua porção inteira é {}".format(n, int(n)))
