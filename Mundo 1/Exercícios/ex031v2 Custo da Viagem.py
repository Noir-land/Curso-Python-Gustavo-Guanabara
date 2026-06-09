"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas
"""

'''d = float(input("Digite a distancia a percorer: "))
if d <= 200:
    v = d * 0.50
else:
    v = d * 0.45
print("A distancia percorrida é {} e o valor a pagar é R$: {}".format(d, v))'''

d = float(input("Digite a distancia: "))
v = d * 0.50 if d <= 200 else d * 0.45
print("Você pagara {}".format(v))
