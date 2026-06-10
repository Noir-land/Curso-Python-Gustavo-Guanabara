"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep
listaA = list()
temp = list()
resp = int(input('Quantos jogos deseja gerar? ').strip())
print('=-=' * 18)
print(f'{"Jogos da MEGA":^48}')
for jogos in range(0, resp):
    contador = num = 0
    while contador < 6:
        num = randint(1, 61)
        if num not in temp:
            temp.append(num)
            contador += 1
    temp.sort()
    listaA.append(temp[:])
    temp.clear()
print('=-=' * 18)
jogo = 0
for i, linha in enumerate(listaA):
    print(f'O {i+1}º jogo: ', end='')
    print(f'{linha}')
    sleep(0.5)
print('=-=' * 18)
print(f'{"Fim de jogo":^48}')
