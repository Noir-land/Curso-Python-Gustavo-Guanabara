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
