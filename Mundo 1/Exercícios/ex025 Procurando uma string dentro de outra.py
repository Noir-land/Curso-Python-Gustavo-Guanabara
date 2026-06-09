"""
Crie um programa que leia o nome de uma pessoa e 
diga se ela tem "Silva" no nome
"""

nome = str(input("Digite um nome: ")).strip()
print("Você tem Dias no nome ? {}".format('Dias' in nome.title()))
