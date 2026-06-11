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
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Em ordem de {inicio} até {fim} seguindo de {passo} em {passo}')
    sleep(1)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.2)
            cont += passo
        print('Fim!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.2)
            cont -= passo
        print('Fim')


cont = list()
contador(1, 10, 1)
contador(10, 0, 2)
cont.append([
    int(input('Digite o inicio: ')),
    int(input('Digite o fim: ')),
    int(input('Digite o passo: '))
])

contador(cont[0][0], cont[0][1], cont[0][2]) # Ou -cont[-1][0]... 