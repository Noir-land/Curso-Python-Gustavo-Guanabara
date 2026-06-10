"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.
No final, mostre:
Quantas pessoas foram cadastradas
A média de idade do grupo
uma lista com todas as mulheres
uma lista com todas as pessoas com idade acima da média.
"""

dados = list()
pessoa = dict()
idade_total = 0
while True:
    pessoa['Nome'] = str(input('Nome: ').strip().capitalize())
    pessoa['Idade'] = int(input('Idade: ').strip())
    idade_total += pessoa['Idade']
    sexo = str(input('Sexo:[M/F] ').strip().capitalize())
    while sexo not in 'FM':
        print('Digite corretamente. M para masculino e F para feminio')
        sexo = str(input('Sexo:[M/F] ').strip().capitalize())
    pessoa['Sexo'] = sexo
    dados.append(pessoa.copy())
    while resp not in 'SN':
        resp = str(input('Deseja continuar?[S/N] ').strip().capitalize())
    if resp[0] == 'N':
        break
print('-='*20)
print(f'Foram cadastrada um total de {len(dados)} pessoas.')
print(f'A idade media é de {idade_total/len(dados):.2f} anos ')
print('As mulheres cadastradas foram: ', end='')
for i, pe in enumerate(dados):
    if pe['Sexo'] == 'F':
        print(f'{pe["Nome"]}', end=' ')
print()
print('-='*20)
print('Pessoas que estão acima da média. ')
for i, pe in enumerate(dados):
    if pe['Idade'] > (idade_total/len(dados)) and pe['Sexo'] == 'M':
        for k, v in pe.items():
            print(f'{k} = {v}; ', end='')
        print('')
    if pe['Idade'] > (idade_total/len(dados)) and pe['Sexo'] == 'F':
        for k, v in pe.items():
            print(f'{k} = {v}; ', end='')
        print('\n')