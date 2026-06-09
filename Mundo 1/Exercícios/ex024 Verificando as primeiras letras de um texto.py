"""
Crie um programa que leia o nome de uma cidade e
diga se ela começa ou não com a palavra "Santo"
"""

'''frase = str(input("Digite seu nome:")).strip()
n = frase.upper()
print("Existem {} letras ao todo".format(n.find("Santo")))'''
frase = str(input("nome ")).strip()
n0 = frase.title()
n = "Santo" in n0[:5]
print("{}".format(n))
