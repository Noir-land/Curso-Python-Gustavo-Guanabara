"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos dólares ela pode comprar
"""

n = float(input("Coloque o valor que deseja converter de reais para dolar: R$"))
dolar = n / 4.28
print("R$:{:.2f} é convertido para USS:{:.2f}".format(n, dolar))
