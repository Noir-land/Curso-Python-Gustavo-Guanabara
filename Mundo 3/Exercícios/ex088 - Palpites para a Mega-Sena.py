"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""

import random
listaA = list()
temp = list()
resp = int(input('Quantos jogos deseja gerar? ').strip())

print('=-=' * 18)
print(f'{"Jogos da MEGA":^48}')
for jogos in range(0, resp):
    contador = num = 0
    while contador < 7:
        contador += 1
        num = random.randint(1, 61)
        temp.append(num)
        for p, i in enumerate(temp):
            if len(temp) > 1:
                if num == i:
                    temp.pop()
                    contador -= 1
                if num not in temp:
                    temp.append(num)
                    contador += 1
    temp.sort()
    listaA.append(temp[:])
    temp.clear()
print('=-=' * 18)
jogo = 0
for j in range(0, resp):
    jogo += 1
    print(f'O {jogo}º jogo:', end='')
    print(f'{listaA[j]}')
print('=-=' * 18)
print(f'{"Fim de jogo":^48}')
