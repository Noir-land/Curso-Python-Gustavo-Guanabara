"""
Faça um programa que leia o comprimento do cateto oposto (co) e 
do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""

o = float(input("O tamanho do cateto oposto: "))
a = float(input("O tamanho do cateto adjacente: "))
h = (o ** 2 + a ** 2) ** (1/2)
print("A Hipotenusa vai medir {:.2f}".format(h))
