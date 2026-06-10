"""
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

lista_de_numero = []
loop = True
while loop:
    num = input('Digite um número: ')
    num_found = False
    for i, p in enumerate(lista_de_numero):
        if p == num:
            num_found = True
            print(f'dentro for {p}')
            break
    if not num_found:
        lista_de_numero.append(num)
    resp = input('Deseja continuar?[S/N] ').upper()
    if resp == 'N':
        loop = False
lista_de_numero.sort()

print(f'final. numeros adicionados foram', end=' ')
for i in lista_de_numero:
    print(f'{i},', end=' ')
