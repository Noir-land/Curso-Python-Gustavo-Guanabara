"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""


from time import sleep

def maior_numero(*num):
    maior = 0
    print('~~~'*20)
    print('Os numeros são: ', end='')
    for n in num:
        print(f'{n} ', end='', flush=True)
        sleep(0.2)
        if n > maior:
            maior = n
    print()
    print(f'Foram apresentados {len(num)} numeros, e o maior numero {maior}')


maior_numero(1, 2)
maior_numero(9, 5, 4, 2, 8)
maior_numero(1,5,9,6,3,1)
maior_numero()