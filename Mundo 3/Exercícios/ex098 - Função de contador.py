"""
Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros:
início, fim e passo
E realize a contagem

Seu programa tem que realizar três contagens através da função criada

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contagem personalizada

"""
from time import sleep

def contador(inicio, fim, passo):
    passo = str(passo)
    fim = str(fim)
    if passo == '0':
        if '-' in fim[0] or '0' in fim[0]:
            passo = '1'
    print(f'Em ordem de {inicio} até {fim} seguindo de {passo} em {passo}')
    passo = '-'+passo
    if '-' in passo[0] or '-' in fim[0] or fim == '0':
        passo = int(passo)
        fim = int(fim)
        for n in range(inicio, fim-1, passo):
            print(f'{n}', end=' ')
    else:
        passo = int(passo)
        fim = int(fim)
        for n in range(inicio, fim+1, passo):
            print(f'{n}', end=' ')
    print('Fim!')


def contador_1_10(inicio, fim, passo):
    print(f'Em ordem de {inicio} até {fim} seguindo de {passo} em {passo}')
    for n in range(inicio, fim+1, passo):
        print(n, end=' ')
    print('Fim!')


def contador_10_0_2(inicio, fim, passo):
    print(f'Em ordem de {inicio} até {fim} seguindo de {passo} em {passo}')
    for n in range(inicio, fim+1, passo):
        print(n, end=' ')
    print('Fim!')


cont = list()
contador_1_10(1, 10, 1)
contador_10_0_2(10, 0, -2)
cont.append([
    int(input('Digite o inicio: ')),
    int(input('Digite o fim: ')),
    int(input('Digite o passo: '))
])

contador(cont[0][0], cont[0][1], cont[0][2]) # Ou cont[-1][0]... 
