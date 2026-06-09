"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando
a estrutura while
"""

p = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão da PA:"))
t = p
c = 1
while c <= 10:
    print(f'{t} > ', end='')
    t += r
    c += 1
print("Acabou")
