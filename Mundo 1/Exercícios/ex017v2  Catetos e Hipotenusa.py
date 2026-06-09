"""
Faça um programa que leia o comprimento do cateto oposto (co) e 
do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""

from math import hypot
co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente:"))
# hi = .hypot(co, ca)
print("A soma dos catetos é igual a {:.2f} hipotenusa".format(hypot(co, ca)))
