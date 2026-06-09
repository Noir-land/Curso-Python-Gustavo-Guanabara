'''
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:
Se ele ainda vai se alistar ao serviço militar
Se é a hora de se alistar
Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''


import datetime
ano = int(input("Em que ano você nasceu? "))
idade = datetime.date.today().year - ano
print("Você nasceu em {} e tem {} anos em {}".format(ano ,idade , datetime.date.today().year))
if idade > 19:
    print("Ja passou do tempo de alistamento em {} anos ".format(idade - 18))
elif idade == 18:
   print("ALISTESSE JA")
elif idade < 18:
    print("Ainda faltando {} anos.".format(18- idade))

