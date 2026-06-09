"""
Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento
"""

n = float(input("Digite o valor do seu salarario para o reajuste:R$"))
r = n*15/100
r2 = r + n
print("O seu salario de {} apos o reajuste de 15% é de {}".format(n, r2))
