"""
Crie um programa onde o usuário possa digitar
sete valores numéricos
e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares
em ordem crescente.
"""

listaPrincipal = [[], []]
tempIimpar = list()
tempPar = list()
for i in range(1, 5):
    numero = int(input(f'Digite o {i}º número: '))
    if numero % 2 == 0:
        listaPrincipal[0].append(numero)
    if numero % 2 == 1:
        listaPrincipal[1].append(numero)

listaPrincipal[0].sort()
listaPrincipal[1].sort()

print(f'Os números  pares  foram: {listaPrincipal[0]}')
print(f'Os números impares foram: {listaPrincipal[1]}')
