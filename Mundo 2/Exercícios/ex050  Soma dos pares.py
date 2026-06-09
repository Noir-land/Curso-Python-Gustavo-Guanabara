"""
Desenvolva um programa que leia seis números inteiros e m
ostre a soma apenas daqueles que forem pares
Se o valor digitado for ímpar, desconsidere-o.
"""

'''soma = 0
cont = 0
for c in range(1, 501,):
    if c % 2 == 0:
        soma += c
        cont += 1
print(f"A soma dos numeros pares é igual a {soma} e seus numeros pares são {cont}")'''
soma = 0
cont = 0
for r in range(1, 7):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"foram {cont} e a soma é  {soma}")

# soma += num
# if soma % 2 == 0:
# print(f"{soma}")
