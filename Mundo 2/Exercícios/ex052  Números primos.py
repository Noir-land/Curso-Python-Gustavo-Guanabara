"""
Faça um programa que leia um número inteiro e
diga se ele é ou não um número primo
"""

num = int(input("Digite um numero: "))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=" ")
        cont += 1
    else:
        print('\033[34m', end=" ")
    print(c, end=" ")
print(f'\033[m\nO numero {num} é divisivel {cont} vezes ')
if cont == 2:
    print("É PRIMO")
else:
    print("NÃO É PRIMO")
