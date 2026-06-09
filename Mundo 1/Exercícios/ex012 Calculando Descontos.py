"""
Faça um algoritmo que leia o preço de um produto e 
mostre seu novo preço, com 5% de desconto
"""

n = float(input("Digite o valor do produto: R$"))
r = 5/100 * n
r2 = n - r
print("O produtor vale {} e com o desconto de 5% ele custara {}".format(n, r2))
