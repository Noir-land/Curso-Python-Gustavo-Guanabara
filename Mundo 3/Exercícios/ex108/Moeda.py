def moeda(msg):
    return f'R${msg:.2f}'


def aumentar(msg, sit=False):
    msg *= 2
    if sit:
        return f'{moeda(msg)}'
    else:
        return msg


def diminuir(msg, sit=False):
    msg -= msg
    if sit:
        return f'{moeda(msg)}'
    else:
        return msg


def dividir(msg, sit=False):
    msg /= 2
    if sit:
        return f'{moeda(msg)}'
    else:
        return msg


def porcento(msg, p=0, sit=False):
    msg = msg / 100 * p
    if sit:
        return f'{moeda(msg)}'
    else:
        return msg


def menos_porcento(msg, p=0, sit=False):
    msg = msg - (msg / 100 * p)
    if sit:
        return f'{moeda(msg)}'
    else:
        return msg
