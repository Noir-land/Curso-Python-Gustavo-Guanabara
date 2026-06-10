"""
Crie um programa que crie uma matriz 3.3
e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela com a formatação correta
"""

matriz = list()
listaDeNumero = list()
for linha in range(0, 2):
    for coluna in range(0, 2):
        listaDeNumero.append(int(input(f'Digite o valor para F2 [{linha}, {coluna}]: ')))
    matriz.append(listaDeNumero[:])
    listaDeNumero.clear()
print('')
for linha in range(0,2):
    for coluna in range(0,2):
        print(f'[{matriz[linha][coluna]}] ', end='')
    print('')
