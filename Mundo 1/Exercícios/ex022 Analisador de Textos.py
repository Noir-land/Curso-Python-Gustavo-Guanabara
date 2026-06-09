"""
Crie um programa que leia o nome completo de uma pessoa:
"""

frase = str(input("Digite seu nome:")).strip()
print("Com todas as letras maiuscula:{} ".format(frase.upper()))
print("Com todas as letras minusculas: {}".format(frase.lower()))
print("Existem {} letras ao todo".format(len(frase) - frase.count(" ")))
s = frase.split()
print("O primeiro nome tem {} letras".format(len(s[0])))
