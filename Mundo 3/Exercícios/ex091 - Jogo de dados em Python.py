"""
Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado
"""

from random import randint

jogos = dict()
Jogador = list()
jogosDicOrdenados = dict()
cont = 0
for j in range(1, 6):
    jogos[f'Jogador{j}'] = randint(1, 6)
    print(f'O Jogador{j} tirou {jogos[f'Jogador{j}']} no dado. ')
for jogado, numero in jogos.items():
    Jogador.append([jogado, numero])
# jogosOrdenados = sorted(Jogador, key=lambda x: x[1], reverse=True)
n = len(Jogador)
for i in range(n):
    for j in range(0, n - i - 1):
        # Queremos do MAIOR para o MENOR, então se o atual for MENOR que o próximo, trocamos.
        if Jogador[j][1] < Jogador[j + 1][1]:
            # Faz a troca manual de posições (substituição direta)
            substituto = Jogador[j]
            Jogador[j] = Jogador[j + 1]
            Jogador[j + 1] = substituto

for k, v in enumerate(Jogador):
    for valor in v:
        jogosDicOrdenados[f'{v[0]}'] = valor

print('-='*22)
print(f'{" ":<10}{"Ranking de Jogadores":>10}{" ":>10} ')
print('--'*22)
for k, v in jogosDicOrdenados.items():
    cont += 1
    print(f' {cont}º lugar ', end='')
    print(f' "{k}" com {v}')
print('--'*22)
