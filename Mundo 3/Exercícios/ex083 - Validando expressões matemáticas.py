"""
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses.
Seu aplicativo deverá analisar se a expressão passada 
está com os parênteses abertos e fechados na ordem correta.
"""

lista = list()
cont = 0
lista.append(str(input('Digite a expressão: ')))
for valores in lista:
    for pos, valor in enumerate(valores):
        if valor[:2] == '(':
            cont += 1
    for pos, valor in enumerate(valores):
        if valor == ')':
            cont += 1

if cont % 2 == 0:
    print(f'Expresão correta')
else:
    print('Expressão errada')
