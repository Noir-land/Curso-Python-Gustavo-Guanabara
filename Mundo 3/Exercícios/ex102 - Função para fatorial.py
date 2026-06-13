"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(num=1, show=False):
    '''
    Esta função calcula o fatorial, e se requisitado, mostrara o calculo.
    num: Recebe o número do fatorial
    show: Mostrar ou não mostrar, o calculo do fatorial
    return: Retornar o fatorial de num.

    Se necessario mostrar o calculo, use o exemplo como base:
    ex: fatorial(5, True)
    '''
    from time import sleep
    fat = 1
    if show == True:
        for n in range(num, 0, -1):
            fat *= n
            print(n, end=' ')
            print('x ' if n > 1 else '= ', end='', flush=True)
            sleep(0.2)
    else:
        for n in range(num, 0, -1):
            fat *= n
    print(fat)


número = int(input('Digite o numero do fatorial: '))
opc = str(input('Deseja mostrar o calculo do fatorial ? ').strip().capitalize())
if 'S' in opc[0]:
    opc = True
fatorial(número, opc)
help(fatorial)
