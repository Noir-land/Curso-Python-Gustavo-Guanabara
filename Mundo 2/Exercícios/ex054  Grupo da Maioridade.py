"""
Crie um programa que leia o ano de nascimento de sete pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores
"""

from datetime import date
atual = date.today().year
menores = 0
maior = 0
for ps in range(1, 3):
    ano = int(input(f"Em que ano a pessoa {ps}º nasceu? "))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menores += 1
print(f"Existem {maior} maiores de idade ")
print(f"Existem {menores} menores de idade.")
