"""
Faça um programa que leia uma frase qualquer e mostre:
Quantas vezes aparece a letra "a"
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez
"""

frase = str(input("Digite uma frase: ")).strip()
n = frase.upper()
print("A letra A aparece na posição: {}".format(n.count("A")))
print("A primeira letra A pareceu na posição: {}".format(n.find("A")+1))
print("A ultima letra A parece na posição: {}".format(n.rfind("A")+1))
