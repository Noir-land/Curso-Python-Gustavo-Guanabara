"""
Faça um programa que leia um número qualquer e mostre
o seu fatorial.
exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
"""

n = int(input("Digite um numero para obeter o factorial. "))
f = 1
print(f'{n}! = ', end='')
for c in range(n, 0, -1):
    print(f'{c}', end="")
    print(" x " if c > 1 else " = ", end='')
    f *= c
print(f)
