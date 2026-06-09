"""
Faça um programa que leia um número qualquer e mostre
o seu fatorial.
exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
"""

'''c = 0
while c < 10:
    print(c)
    c += 1'''
num = int(input("Digite o numero para... "
                "\ncalcular o factorial"))
c = num
f = 1
print(f"calculando {num}! = ", end='')
while c > 0:
    print(f'{num}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f"{f}")
