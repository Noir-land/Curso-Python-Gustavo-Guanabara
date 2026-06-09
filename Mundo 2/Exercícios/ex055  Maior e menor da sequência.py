"""
Faça um programa que leia o peso de cinco pessoas
No final, mostre qual foi o maior e o menor peso lidos
"""

menor = 0
maior = 0
for pes in range(1, 5):
    peso = float(input(f"Qual peso da {pes}º pessoa? "))
    if pes == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(maior)
print(menor)
