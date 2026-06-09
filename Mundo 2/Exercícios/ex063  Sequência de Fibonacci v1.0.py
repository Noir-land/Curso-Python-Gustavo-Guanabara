"""
Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os primeiros n elementos e uma sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 (...)
"""

sequence = int(input("Digite quantas sequecias iram aparecer: "))
num = 0
num2 = 1
print(f"{num} > {num2}", end=' ')
cont = 3
while cont <= sequence:
    num3 = num + num2
    print(f"> {num3}", end=' ')
    num = num2
    num2 = num3
    cont += 1

print("fim")
