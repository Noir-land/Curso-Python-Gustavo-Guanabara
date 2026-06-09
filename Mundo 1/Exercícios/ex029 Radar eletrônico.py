"""
Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite.
"""

v = float(input("Velocidade do carro: "))
m = (v-80) * 7
if v > 80:
    print('Voce passou de 80Km/h.A multado é R$:{}'.format(m))
print("DIRIJA COM SEGURANÇA!")
