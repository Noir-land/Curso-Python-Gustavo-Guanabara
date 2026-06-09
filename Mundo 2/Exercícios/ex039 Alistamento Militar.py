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

