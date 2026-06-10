"""
Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado
"""

from random import randint
from time import sleep
from operator import itemgetter

jogos = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)
         }
rank = list()
for jogador, dado in jogos.items():
    print(f'O {jogador} tirou {dado}')
rank = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('-='*22)
print(f'{" ":<10}{"Ranking de Jogadores":>10}{" ":>10} ')
print('--'*22)
for i, v in enumerate(rank):
    print(f'{i+1}º lugar. {v[0]} com {v[1]}')
print('--'*22)
