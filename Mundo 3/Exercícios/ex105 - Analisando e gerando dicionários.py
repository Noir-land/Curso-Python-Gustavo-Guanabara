"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
quantidade de notas
a maior nota
a menor nota
a média da turma
a situação (opcional)
Adicione tambeem as docstrings da função
"""


def notas(*nota, situacao=False):
    '''
    Esta função calcula nota e mostra a situação do aulo.
    nota: recebe uma quantidade indefinida de valores.
    situação: Permite a mostragem da situação do aluno.
    return: retorna a nota do aluno e situação se for requisitado.
    '''
    nota_aluno = dict()
    nota_aluno['total'] = len(nota)
    maior = menor = soma = media = 0
    for n in nota:
        soma += n
        if n > maior:
            maior = n
            nota_aluno['maior'] = maior
        if n < menor or menor < maior:
            menor = n
            nota_aluno['menor'] = menor
        media = soma / len(nota)
        nota_aluno['media'] = media
    if situacao == True:
        if media >= 8:
            nota_aluno['situação'] = 'OTIMA '
        elif media >= 7:
            nota_aluno['situação'] = 'BOA'
        elif media >= 6:
            nota_aluno['situação'] = 'RAZOAVEL'
        else:
            nota_aluno['situação'] = 'RUIM'
    return nota_aluno


aluno = notas(5.5, 7, 5, 6, 8, 7, 1, 1, situacao=True)

print(aluno)
help(notas)
