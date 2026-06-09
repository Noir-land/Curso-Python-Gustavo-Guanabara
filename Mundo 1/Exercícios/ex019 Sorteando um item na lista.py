"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.
"""

import random
a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno ")
l = [a1, a2, a3]
r = random.choice(l)
print("O Aluno escolhido foi {}".format(r))
