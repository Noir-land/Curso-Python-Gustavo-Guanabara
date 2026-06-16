def moeda(msg):
    return f'R${msg:.2f}'.replace('.',',')


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


def resumo(msg, pmais=0, pmenos=0):
    print('~~'*20)
    print(f'{"O RESUMO do Valor":>28}')
    print('~~'*20)
    lista_de_valores = {'Preço analisado': {moeda(msg)},
                        'Dobro do preço': {aumentar(msg, True)},
                        f'A metade de {moeda(msg)}': {dividir(msg, True)},
                        f'{pmais}% de aumento {moeda(msg)}': {porcento(msg, pmais, True)},
                        f'{pmenos}% de redução {moeda(msg)}': {menos_porcento(msg, pmenos, True)}
                        }
    for k, v in lista_de_valores.items():
        for valor in v:
            print(f'{k + ':':<30}', end=' ')
            print(f'{valor}')
    print('~~'*20)

