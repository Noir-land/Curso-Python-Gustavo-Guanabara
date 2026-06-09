import random
jogador = int(input('''
SUAS OPÇÕES:
 [0] PEDRA
 [1] PAPEL
 [2] TESOURA
 Qual a sua escolha: '''))
l = ['PEDRA', 'PAPEL', 'TESOURA']
c = random.randint(0, 2)
print("~"*25)
print(f"Maquina jogou {l[c]} ")
print(f"Jogador jogou {l[jogador]}")
print("~"*25)
if c == 0:  # maquina jogou pedra
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("MAQUINA VENCE")
    else:
        print("JOGADA INVALIDA")
elif c == 1:  # maquina jogou papel
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print("JOGADA INVALIDA")
elif c == 2:  # maquina jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('MAQUINA VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print("JOGADA INVALIDA")
