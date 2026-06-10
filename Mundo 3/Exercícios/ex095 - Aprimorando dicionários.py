"""
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes de aproveitamento 
de cada jogador.
"""

Jogadores = list()
Jogador = dict()
gols = list()
while True:
    Jogador['Nome'] = str(input('Nome do jogador: ').strip().capitalize())
    qnt_jogos = int(input('Quantidade de jogos: ').strip())
    tot_gols = 0
    for n in range(0, qnt_jogos):
        gols.append(int(input(f'Quantos gold foram feitos na {n+1}º partida? ').strip()))
        tot_gols += gols[n]
    Jogador['Gols'] = gols[:]
    Jogador['Gols Totais'] = tot_gols
    Jogadores.append(Jogador.copy())

    resp = str(input('Deseja continuar?[S/N]').strip().capitalize())
    if resp[0] == 'N':
        break
print('--'*20)
print(f'{"Cod":<4}{"Nome":<7}{"Gols":<7}{"Total":>2}')
for i, v in enumerate(Jogadores):
    print(f'{i}', end=' '*3)
    for k, j in v.items():
        print(f'{j}', end=' '*4)
    print()
while True:
    print('--'*20)
    while True:
        opc = input('Qual jogador deseja visualizar? [999 para sair] ')
        if not opc.isdigit():
            print(f'ERRO! Digite apenas números de 0 a {len(Jogadores)}.')
            continue
        opc = int(opc)
        if opc == 999 or 0 <= opc <= len(Jogadores):
            break
    print('-='*20)
    print(f'==>O levantamento do jogador {Jogadores[opc]['Nome']}')
    for i, v in enumerate(Jogadores):
        for i, n in enumerate(gols):
            print(f'=> Na {i+1}º partida, marcou {n} gols.')
        print(f'=>Foi um total de {tot_gols} gols.')
    if opc == 999:
        break
        
