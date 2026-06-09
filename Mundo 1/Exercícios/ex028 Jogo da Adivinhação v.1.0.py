"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

import random
from time import sleep
p = int(input("Digite um numero de 1 a 5: "))
r = random.randint(1, 5)
print('PROCESSANDO....')
sleep(1)
print("O numero é {}".format(r))
if p == r:
    print("Parabens você acertou.")
else:
    print("Boa sorte na proxima.")
