"""
Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
A média de idade do grupo
Qual é o nome do homem mais velho
Quantas mulheres têm menos de 20 anos
"""

sex = str(input("Digite seu sexo: ")).upper().strip()[0]
while sex not in "MnFf":  # QUANDO TEM " "MnFf" É FINALIZADO O LOOP ou QUANDO A AFIRMAÇÃO SE TORNA FALSA
    sex = str(input("Digite seu sexo corretamente: ")).upper().strip()[0]
if sex == 'M':
    sex = 'Masculino'
elif sex == 'F':
    sex = 'Feminino'
else:
    Exception
    'error'
print(f"Parabens, o sexo {sex} foi registrado com sucesso")
