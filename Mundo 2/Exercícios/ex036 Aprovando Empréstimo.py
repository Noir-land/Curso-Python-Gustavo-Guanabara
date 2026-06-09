'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''


casa = float(input("Valor da Casa: "))
salario = float(input("Salario: "))
tempo = int(input("Deseja pagar em ate quantos anos? "))
prestação = casa / (tempo * 12)
minimo = salario * 30 / 100
if prestação <= minimo:
    print("A compra foi PROVADA")
else:
    print("A compra foi NEGADA")
print("Obrigado pela preferencia.")
'''if r < sa:
    print("A venda foi aprovada")
else:
    print("A venda não foi aprovada")'''
