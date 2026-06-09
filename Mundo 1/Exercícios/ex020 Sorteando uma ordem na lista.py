"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
 Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

import random
a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terciero aluno: ")
a4 = input("Quarto aluno: ")
lista = [a1, a2, a3, a4]
r1 = random.shuffle(lista)
# r2 = random.choice(lista)
# r3 = random.choice(lista)
print("A ordem de sorteio foi".format(r1))
print(lista)
