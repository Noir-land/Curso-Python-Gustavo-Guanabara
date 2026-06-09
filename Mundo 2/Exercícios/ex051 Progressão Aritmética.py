"""Desenvolva um programa que leia o primeiro termo e a razão
de uma PA (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão.
"""

prim = int(input("Digite o primeiro termo: "))
raz = int(input("Razão: "))
dt = prim + (10-1) * raz
for c in range(prim, dt+raz, raz):
    print(f"{c}", end=">>")
print("Acabou")
