"""
Faça um programa que leia nome e peso de várias pessoas
guardando tudo em uma lista.
No final, mostre:
quantas pessoas foram cadastradas.
uma listagem com as pessoas mais pesadas
uma listagem com as pessoas mais leves
Obs.: Gerar uma lista com os mais leves e mais pesados
Vai depender de analisar qual é o mais leve e o mais pesado.
Se houver mais de um com esse peso, insere na lista.
O mais normal é que a lista de mais pesados tenha apenas 1 pessoa,
que é o motivo pelo qual a lista existe.
"""

pessoas = list()
temp = list()

pesominimo = pesomaximo = 0
while True:
    temp.append(str(input('Nome: ').capitalize().strip()))
    temp.append(float(input('Peso: ')))
    if len(temp) == 0:
        pesominimo = pesomaximo = temp[1]
    else:
        if temp[1] > pesomaximo:
            pesomaximo = temp[1]
        if temp[1] < pesominimo:
            pesominimo = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = (str(input('Deseja continuar?[S/n]   ').strip().upper()))
    if resp[0] in 'N':
        break

print(f'O numero pessoas cadastradas foi {len(pessoas)}')
print(f'O maior peso foi {pesomaximo}Kg. ', end='')
for pessoa in pessoas:
    if pessoa[1] == pesomaximo:
        print(f'[{pessoa[0]}] ', end='')
print()
print(f'O menor peso foi {pesominimo}Kg. ', end='')
for pessoa in pessoas:
    if pessoa[1] == pesominimo:
        print(f'[{pessoa[0]}] ', end='')
