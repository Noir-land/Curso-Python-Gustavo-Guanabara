"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas
"""

d = int(input("Distancia a percorrer em Km: "))
p = d * 0.50
p2 = d * 0.45
if d <= 200:
    print("Valor a pagar R$:{}".format(p))
else:
    print("O valor a pagar é {}".format(p2))
