'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
até 9 anos: mirim
até 14 anos: infantil
até 19 anos: júnior
até 20 anos: sênior
acima de 20: master
'''

from datetime import date
atual = date.today().year
ano = int(input("Digite o ano de nascimento do atleta: "))
idade = atual - ano
print('''O atleta tem {} anos.'''.format(idade))
if idade <= 9:
    print("CLASSIFICAÇÃO: MIRIM.")
elif idade <= 14:
    print("CLASSIFICAÇÃO: INFANTIL.")
elif idade <= 19:
    print("CLASSIFICAÇÃO: jUNIOR.")
elif idade <= 25:
    print("CLASSIFICAÇÃO: SÊNIOR.")
else:
    print("CLASSIFICAÇÃO: MASTER.")
