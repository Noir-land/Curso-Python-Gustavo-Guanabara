"""
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""

listanum = []
for i in range(3):
    numero = int(input('Digite um numero: '))
    if len(listanum) == 0:  # if i == 0 or numero > listanum[-1]:
        listanum.append(numero)
    else:
        if numero < listanum[0]:
            listanum.insert(0, numero)
        elif numero > listanum[-1]:
            listanum.append(numero)
        else:
            for i in listanum:
                listanum.insert(i, numero)
                break
print(listanum)
