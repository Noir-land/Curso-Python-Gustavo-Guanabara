"""
Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e
a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
"""

n = float(input("Altura da parede: "))
n2 = float(input("Largura da parede: "))
print("A dimensão {}x{} é igual a {}m²\nPara pintar {}m² é necessario {}lt de tinta".format(n, n2,(n*n2), (n*n2), (n*n2)/2))
