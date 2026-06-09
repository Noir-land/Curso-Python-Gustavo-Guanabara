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
