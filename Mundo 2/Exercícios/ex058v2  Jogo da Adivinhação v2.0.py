"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer
"""

from random import randint
comp = randint(0, 11)
print("Sou a maquina, tente acerta o numero...")
acertou = False
chances = 0
while not acertou:
    jogador = int(input("Qual o numero: "))
    chances += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print("É um numero maior, tente novamente")
        elif jogador > comp:
            print("É um numero menor, tente novamente")
print(f"Acertou na {chances}º tentativa. Parabens")
