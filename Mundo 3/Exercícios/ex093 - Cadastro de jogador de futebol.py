"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""

Jogador = dict()
gols = list()
Jogador['Nome'] = str(input('Nome do jogador: ').strip().capitalize())
qnt_jogos = int(input('Quantidade de jogos: ').strip())
tot_gols = 0
for n in range(0, qnt_jogos):
    gols.append(int(input(f'Quantos gold foram feitos na {n+1}º partida? ').strip()))
    tot_gols += gols[n]
Jogador['Gols'] = gols[:]
Jogador['Gols Totais'] = tot_gols
print('-='*20)
for key, values in Jogador.items():
    print(f'O campo {key:^7} tem o valor {values}. ')
print('-='*20)
print(f'O jogador {Jogador["Nome"]} jogou {qnt_jogos} partidas.')

for i, n in enumerate(gols):
    print(f'  => Na {i+1}º partida, marcou {n} gols.')
print(f'Foi um total de {tot_gols} gols.')
