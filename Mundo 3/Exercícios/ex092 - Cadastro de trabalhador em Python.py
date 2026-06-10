"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de zero, o dicionário receberá também
o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.
Obs.: Aposentadoria em 35 anos de contribuição.
"""



from datetime import date
carteira_de_trabalho = {'Nome': '',
                        'Idade': '',
                        'Ctps': 0,
                        }
carteira_de_trabalho['Nome'] = str(input('Nome: ').strip().capitalize())
ano_de_nascimento = int(input('Digite a data de nascimento: ').strip())
carteira_de_trabalho['Idade'] = date.today().year - ano_de_nascimento
carteira_de_trabalho['Ctps'] = int(input('Carteira de trabalho:[0 não tem] ').strip())
if carteira_de_trabalho['Ctps'] == 0:
    carteira_de_trabalho['Ctps'] = 'Sem carteira assinada'
else:
    carteira_de_trabalho['Contratação'] = int(input('Data de contratação: ').strip())
    carteira_de_trabalho['Salario'] = float(input('Seu salario: ').strip())
    carteira_de_trabalho['Aposentadoria'] = (carteira_de_trabalho['Contratação'] + 35) - ano_de_nascimento
print('-='*20)
for k, v in carteira_de_trabalho.items():
    print(f'{k:<5} tem a seguinte informação: {v}')
