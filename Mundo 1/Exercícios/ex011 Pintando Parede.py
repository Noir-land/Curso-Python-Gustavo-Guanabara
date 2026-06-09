"""Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e
a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
"""

n = float(input("Largura da parede: "))
n2 = float(input("Altura da parede: "))
r = n*n2
r2 = r / 2
print("A dimensão de trabalho é de {}x{} e sua area de trabalho é de {}m².".format(n, n2, r))
print('Para pintar a parede é necessario {}lt de tinta'.format(r2))
