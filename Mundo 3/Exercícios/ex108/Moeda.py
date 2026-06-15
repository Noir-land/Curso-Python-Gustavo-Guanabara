def moeda(msg):
    return f'R${msg:.2f}'


def aumentar(msg, sit=False):
    msg *= 2
    return msg


def diminuir(msg, sit=False):
    msg -= msg
    return msg


def dividir(msg, sit=False):
    msg /= 2
    return msg


def porcento(msg, p=0, sit=False):
    msg = msg / 100 * p
    return msg


def menos_porcento(msg, p=0, sit=False):
    msg = msg - (msg / 100 * p)
    return msg
