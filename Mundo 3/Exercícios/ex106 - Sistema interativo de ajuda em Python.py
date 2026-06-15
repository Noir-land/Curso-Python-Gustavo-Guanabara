"""
Faça um minissistema que utilize o interactive help do Python
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra "FIM", o programa se encerrará!.
OBS: use cores.
"""


def ajuda(msg):
    '''
    Função que ajuda o usuario a acessar informçções sobre o comando
    msg: recebe a string a ser requisitada 
    return: retorna as informações

    '''
    from time import sleep
    sleep(0.5)
    while True:
        if msg != 'Fim':
            cabecalho(f'ACESSANDO O MANUAL DO COMANDO "{opc}"')
            print(f'\033[0;32m')
            sleep(0.5)
            print(f'{help(msg)}')
            print(f'\033[m')
            sleep(0.5)
            return


def cabecalho(titulo):
    cores = {'limpar': '\033[m',
             'verde': '\033[0;32m'}
    tmh = len(titulo)
    print('\033[0;30m-=' * len(titulo))
    print(f'{cores['verde']}{titulo:^{tmh * 2}} {cores['limpar']}')
    print('\033[0;30m--\033[m'*len(titulo))


cabecalho('SISTEMA DE AJUDA PYTHON')
while True:
    opc = str(input('Função ou biblioteca: '))
    if opc == 'fim':
        cabecalho('Fim')
        break
    else:
        ajuda(opc)
