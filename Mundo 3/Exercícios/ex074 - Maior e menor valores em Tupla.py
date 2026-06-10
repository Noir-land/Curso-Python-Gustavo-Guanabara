"""
Crie um programa que vai gerar cinco números aleatórios 
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados
e também indice o menor e o maior valor que estão na tupla
"""

import random
# num = (random.randint(1, 50),(random.randint(1, 50)),(random.randint(1, 50)),
#       (random.randint(1, 50)),(random.randint(1, 50))) #funciona para perguntas
# print('Os números sorteados são: ',end='')
# for n in num:
#    print(f'{n} ', end='')
# print(f"\nO maior número é {max(num)}")
# print(f"O menor número é {min(num)}")

a = tuple(random.sample(range(10), 5))
print(
    f'Os números sorteados foram: {a}\nO maior valor é {max(a)} e o menor é {min(a)}.')
