"""
Faça um algoritmo que leia o preço de um produto e 
mostre seu novo preço, com 5% de desconto
"""

p = float(input("Quantos % de desconto deseja aplicar ao produto ? "))
v = float(input("Qual o valor do produto ? R$"))
r = p/100 * v
r3 = r-v
print("Com o desconto de {}% o produto no valor de {} custara {}".format(p, v, r3))
print("O desconto é de R$:{:.2f}".format(r))
