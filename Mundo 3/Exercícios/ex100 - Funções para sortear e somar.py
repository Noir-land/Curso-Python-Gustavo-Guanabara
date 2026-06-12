"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""


from random import sample


def dobrando(lista):
    print(f'Os números par dobrados são: ', end='')
    for i in lista:
        for n in i:
            if n % 2 == 0:
                n *= 2
                print(f'{n} ', end='')
    print()

def somaPar(lista):
    print(f'A soma dos números pars são: ', end='')
    soma = 0
    for i in lista:
        for n in i:
            if n % 2 == 0:
                soma += n
    print(f'{soma} ', end='')

def sorteando(lista):
    sorteado = sample(range(1, 100), 5)
    print(f'Os números sortados foram: ',end='')
    for n in sorteado:
        print(n, end=' ')
    print()
    return lista.append(sorteado)

lista_de_numeros = list()
sorteando(lista_de_numeros)
dobrando(lista_de_numeros)
somaPar(lista_de_numeros)