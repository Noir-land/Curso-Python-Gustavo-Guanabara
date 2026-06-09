"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos dólares ela pode comprar
"""

n = float(input("Quanto reais  você deseja converter em dolares ? R$: "))
print('Com R$:{:.2f} é possivel receber USS:{:.2f}'.format(n, n*0.23))
