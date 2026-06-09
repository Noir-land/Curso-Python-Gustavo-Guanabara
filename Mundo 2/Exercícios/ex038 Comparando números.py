'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
o primeiro valor é maior
o segundo valor é maior
não existe valor maior; os dois são iguais
'''

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
# if num1 < num2:
# print("O primeiro numero é menor")
if num1 > num2:
    print("O primeiro numero  é maior")
elif num2 > num1:
    print("O segundo numero é maior")
# elif num2 < num1:
    # print("O segundo numero é menor")
elif num1 == num2:
    print("Os numeros são iguais")
