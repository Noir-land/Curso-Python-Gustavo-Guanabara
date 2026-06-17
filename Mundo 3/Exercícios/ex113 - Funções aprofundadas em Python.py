"""
Reescreva a função `leiaInt()` que fizemos no desafio 104,
incluindo agora a possobilidade da digitação de um número de tipo inválido.
Aproveite e crie também a função `leiaFloat()` com a mesma funcionalidade.
"""


def leia_int(num=0):
    while True:
        try:
            num = int(input(num))
        except (ValueError, TypeError):
            print('ERRO!  Digite um número inteiro valido. ')
            continue
        else:
            return num


def leia_float(num=0):
    while True:
        try:
            num = float(input(num))
        except (ValueError, TypeError):
            print('ERRO! Digite um número real valido.')
            continue
        else:
            return num


def leia_num(msg=''):
    while True:
        try:
            msg = input('Digite um número: ')
            try:
                num = int(msg)
                return f'O número {num} é valido.'
            except ValueError:
                num = float(msg)
                return f'O número {num} é valido.'
        except (ValueError, TypeError):
            print('ERRO! Digite um número valido.')
        except KeyboardInterrupt:
            return '\nNenhuma informação foi registrada.'


nt = leia_num()
print(nt)
