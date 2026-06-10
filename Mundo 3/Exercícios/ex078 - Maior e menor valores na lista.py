'''
Faça um programa que leia 5 valores números e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados
e as suas respectivas posições na lista.
'''

numlist = []
maior = menor = 0
pos_menor = []
pos_maior = []
for i in range(5):
    n = int(input('digite um numero: '))
    numlist.append(n)
for pos, num in enumerate(numlist):
    if menor == 0:
        menor = num
    if num < menor:
        menor = num
    if num > maior:
        maior = num
for pos, num in enumerate(numlist):
    if num == menor:
        pos_menor.append(pos)
    if num == maior:
        pos_maior.append(pos)

print('Os numeros listados foram', end=' ')
for n in numlist:
    print(f'{n}', end=' ')
print(f'\nO maior numero foi {maior}, na posição ', end='')
for pos in pos_maior:
    print(f'{pos},', end='')
print(f'o menor numero foi {menor}, na posição ', end='')
for pos in pos_menor:
    print(f'{pos},', end='')
print(' ')
