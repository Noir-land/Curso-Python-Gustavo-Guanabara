"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

aluno_status = dict()
aluno_status['Nome'] = str(input('Nome do aluno: ').strip().capitalize())
aluno_status['Nota'] = float(input(f'Média de {aluno_status["Nome"]}: ').strip())
if aluno_status['Nota'] >= 7:
    aluno_status['Estado'] = 'Aprovado.'
elif 5 <= aluno_status['Nota'] < 7:
    aluno_status['Estado'] = 'Recuperação.'
else:
    aluno_status['Estado'] = 'Reprovado.'
print('==='*10)
for k, v in aluno_status.items():
    print(f'{k} é {v}')
    print('---'*10)
estudantes = list()
estudantes.append(aluno_status.copy())
print(estudantes)