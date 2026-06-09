"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
Exemplo.: Ana Maria de Souza
Primeiro = Ana
Último: Souza
"""

nome = str(input("Digite seu nome:")).strip().split()
print("Seu primeiro nome é {}".format(nome[0]))
print(f"Seu ultimo nome é {nome[len(nome)-1]}")
