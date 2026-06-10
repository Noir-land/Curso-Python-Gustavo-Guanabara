"""
Aprimore o desafio anterior, mostrando no final:
a soma de todos os valores pares digitados
a soma dos valores da terceira coluna
o maior valor da segunda linha
"""

matriz = list()
tot3coluna = maior = totpar = 0
num = 1

for linha in range(0, 3):
    temp = list()
    for coluna in range(0, 3):
        temp.append(num)
        num += 1
    matriz.append(temp[:])

print('-' * 40)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

for p, i in enumerate(matriz):
    for n in i:
        if n % 2 == 0:
            totpar += n
    tot3coluna += i[2]
for c in matriz[1]:
    if c > maior:
        maior = c

print('-' * 40)
print(f"{'A soma de todos os números pares é:':<37} {totpar:^5}")
print(f"{'A soma de todos da terceira coluna é:':<37} {tot3coluna:^5}")
print(f"{'O maior valor da segunda linha é:':<37} {maior:^5}")
print('-' * 40)
