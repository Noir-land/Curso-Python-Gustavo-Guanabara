"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
"""

'''ano = int(input("Digite um ano e contenha a resposta se ele é ou não Bissexto: "))
if  ano % 4 == 0: #para nos não multiplo de 100 e não são multiplos de 400: ano 1700 não é bissexto mas é respondido que sim
    print(f"O {ano} é Bissexto.")
else:
    print(f"O{ano} não é Bissexto.")'''

ano = int(input("Digite um ano para saber se ele é ou não Bissexto: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # Correção do erro acima. anos
    print(f"O {ano} é Bissexto.")
else:
    print(f"O {ano} não é bissexto.")
