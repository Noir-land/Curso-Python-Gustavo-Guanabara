"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de R$ 15%.
"""

v = float(input("Valor do salario: "))
a = v * 10 / 100
r1 = a + v
a3 = v * 15 / 100
r2 = a3 + v
if v > 1250:
    print("Você recebera um aumento de 10% o seu novo salario é {}".format(v + a))
else:
    print("Voce recebera um aumento de 15% o seu novo salario é {}".format(v + a3))
