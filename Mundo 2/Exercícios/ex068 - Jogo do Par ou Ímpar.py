from random import randint
vitorias = 0
while True:
    jogador = int(input("Diga um numero:"))
    jogada = ' '
    maquina = randint(1, 10)
    resultado = jogador + maquina
    while jogada not in 'PI':
        jogada = str(input("Par ou Impar ? (P / I) ")).upper().strip()
    print(f"O você jogou {jogador} e a maquina {maquina}. Total de {resultado}", end=" ")
    print("é  Par" if resultado % 2 == 0 else "é Impar")
    if jogada == 'P':
        if resultado % 2 == 0:
            print("Vencedor!!")
            vitorias += 1
        else:
            print('Perdeu')
            break
    elif jogada == 'I':
        if resultado % 2 == 1:
            print('Vencedor!!')
            vitorias += 1
        else:
            print('Perdeu')
            break
print(f'Fim de jogo, foram {vitorias}')
