"""
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos).
Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais
"""

Palavras = ('Comida', 'lanche', 'Pão', 'Queijo', 'Bolo', 'Pizza',
            'Refrigerante', 'Computador',)
for p in Palavras:
    print(f'\nNa plavra {p.upper()} temos', end=' ')
    for Letras in p:
        if Letras.lower() in "aeiou" or Letras.lower() in 'ã':
            print(f'{Letras}', end=' ')
