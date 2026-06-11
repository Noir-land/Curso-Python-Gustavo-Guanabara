"""
Faça um programa que tenha uma função chamada area(), 
que receba dimensões de um terreno retangular (largura e comprimento) e 
mostre a área do terreno
"""


def area(largura, comprimento):
    area_do_terreno = largura * comprimento
    print(f'A área do terreno "{largura} x {comprimento}" é de {area_do_terreno:.1f} m²')
    print()


def cabecalho(titulo):
    tmh = len(titulo)
    print('-=' * len(titulo))
    print(f'{titulo:^{tmh * 2}}')
    print('--'*len(titulo))


cabecalho('CONTROLE DE TERRENOS')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
