"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
exemplo: digite um número: 1834
unidade: 4
dezenas: 3
centenas: 8
milhares: 1
"""

n = int(input("Digite um numero de 0 a 9999 "))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print("O numero {}\nunidade: {}\ndezena:{}\ncentena: {}\nmilhar: {}".format(n, u, d, c, m))
