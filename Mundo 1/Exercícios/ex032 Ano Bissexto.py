'''import calendar
a = int(input("Digite um ano"))
if calendar.isleap(a):
    print("O ano {} é Bissexto".format(a))
else:
    print("O ano {} não é Bissexto".format(a)) '''
import datetime
import calendar
a = int(input("Digite um ano:"))
if a == 0:
    a = datetime.date.today().year  # Para pegar o ano atual da maquina
if calendar.isleap(a):
    print(f"O ano {a} é Bissexto")
else:
    print(f"O ano {a} não é Bissexto")
