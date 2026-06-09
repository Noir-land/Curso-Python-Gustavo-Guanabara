"""
Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo
Inclusive posso dizer qual tipo de triângulo pode ser formado.
Não deve ser difícil isso em Python.
"""

a = float(input("Primeira reta: "))
b = float(input("Segunda  reta: "))
c = float(input("Terceira reta: "))
if a < b + c and b < a + c and c < a + b:
    print(f"E possivel fazer um triangulo")
else:
    print("não é possivel fazer um tringulo")
