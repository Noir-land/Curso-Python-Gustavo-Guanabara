"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(nome='', gols=0):
    if nome == '':
        nome = '< Desconhecido >'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome}, fez {gols} gols')


jogador = str(input('Nome do jogador: ').strip())
gols = str(input('Gols marcados: ').strip())

ficha(jogador, gols)
