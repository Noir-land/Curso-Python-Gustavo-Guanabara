"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
exemplo: digite um número: 1834
unidade: 4
dezenas: 3
centenas: 8
milhares: 1
"""

n = int(input("Digite um numero de 0 a 9999 "))
n1 = str(n)
print("O numero {}\nunidade: {}\ndezena:{}\ncentena: {}\nmilhar: {}".format(n, n1[3], n1[2], n1[1], n1[0]))
