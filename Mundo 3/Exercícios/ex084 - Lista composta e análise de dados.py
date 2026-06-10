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
pessoaspesadas = list()
pessoasleves = list()
pesominimo = pesomaximo = None
while True:
    temp.append(str(input('Nome: ').capitalize().strip()))
    temp.append(float(input('Peso: ')))
    pessoas.append(temp[:])
    temp.clear()
    resp = (str(input('Deseja continuar?[S/n]').strip().upper()))
    if resp[0] in 'N':
        break


print(f'O número pessoas cadastradas foi {len(pessoas)}')
print('As pessoas com maior peso são: ', end='')

for pessoa in pessoas:
    if pessoa[1] >= 80:
        pessoaspesadas.append(pessoa[0])
        if pesomaximo is None or pessoa[1] >= pesomaximo:
            pesomaximo = pessoa[1]
    else:
        pessoasleves.append(pessoa[0])
        if pesominimo is None or pessoa[1] <= pesominimo:
            pesominimo = pessoa[1]

for p in pessoaspesadas:
    print(f'[{p}]', end=' ')
print('\nAs pessoas com menor peso são: ', end='')
for p in pessoasleves:
    print(f'[{p}]', end=' ')

if pesomaximo is None:
    pesomaximo = '-nenhum valor-'
if pesominimo is None:
    pesominimo = '-nenhum valor-'
print(f'\nO maior peso é {pesomaximo} e o menor é {pesominimo}')
