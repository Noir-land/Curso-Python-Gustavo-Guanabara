"""
Crie um programa que tenha a função leia_int(), 
que vai funcionar de forma semelhante à função input do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
ex.:
n = leia_int("Digite um n")
"""


def leia_int(num):
    numero = 0
    while True:
        validacao = str(input(num))
        if validacao.isnumeric():
            numero = validacao
            return numero
        else:
            print('Digite um número inteiro valido')


n = leia_int('Digite um numero: ')
print(f'O número {n} é valido.')
