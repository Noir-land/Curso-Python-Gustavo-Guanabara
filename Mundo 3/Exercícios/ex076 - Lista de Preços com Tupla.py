"""
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos precos,
na sequência
No final, mostre uma listagem de precos,
organizando os dados em forma tabular
"""

ListaDePreço = ('Pão', 0.5,
                'Queijo', 3,
                'Bolo', 7,
                'Pizza', 15,
                'Refrigerante', 5,
                'Computador', 1500)
print('+++++'*10)
print(' '*15, "Lista de Preços")
print('+++++'*10)
for n in range(0, len(ListaDePreço)):
    if n % 2 == 0:
        print(f'{ListaDePreço[n]:.<20}', end='R$ ')
    if n % 2 == 1:
        print(f'{ListaDePreço[n]:>8.2f}')
