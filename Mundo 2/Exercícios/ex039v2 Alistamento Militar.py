'''
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar
Se é a hora de se alistar
Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''


from datetime import date
atual = date.today().year
nasc = int(input("Data de nascimento: "))
idade = atual - nasc
print('Quem nasceu {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print("Você deve se alistar o mais rapido possivel.")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos para se alistar.".format(saldo))
    ano = atual + saldo
    print("Seu alistamento sera em {}".format(ano))
elif idade > 18:
    saldo = idade - 18
    print("Seu alistamento ja passou em {}".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}".format(ano))
