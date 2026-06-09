'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, e acordo com a tabela abaixo:
abaixo de 18.5: abaixo do peso
entre 18.5 e 25: peso ideal
25 até 30: sobrepeso
30 até 40: obesidade
acima de 40: obesidade mórbida
'''

peso = float(input("Quantos kg:"))
altura = float(input("Sua altura em metros: "))
resultado = peso / (altura * altura)
print(f"Seu IMC é de {resultado:.1f}")
if resultado <= 18.5:
    print("ABAIXO DO PESO")
elif resultado <= 25:
    print("PESO IDEAL")
elif resultado <= 30:
    print("SOBREPESO")
elif resultado <= 40:
    print("OBSIDADE")
else:
    print("OBESIDADE MORBIDA")
