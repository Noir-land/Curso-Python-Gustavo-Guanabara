"""
Aprimore o desafio anterior, mostrando no final:
a soma de todos os valores pares digitados
a soma dos valores da terceira coluna
o maior valor da segunda linha
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tot3coluna = maior = totpar = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f'Digite um número:[{linha}, {coluna}] ').strip())
print('-' * 50)
for linha in range(0, 3):
    # Extraindo a soma de todos os numeros da coluna 3
    tot3coluna += matriz[linha][2]
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            totpar += matriz[linha][coluna]
    print()
for c in matriz[1]:
    if c > maior:
        maior = c
print('-' * 50)
print(f"{'A soma de todos os números pares é:':<37} {totpar:^5}")
print(f"{'A soma de todos da terceira coluna é:':<37} {tot3coluna:^5}")
print(f"{'O maior valor da segunda linha é:':<37} {maior:^5}")
print('-' * 50)
