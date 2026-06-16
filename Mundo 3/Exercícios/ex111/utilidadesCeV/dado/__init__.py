def leia_dinheiro(msg):
    numero = 0
    while True:
        variavel = input(msg).replace(',', '.')
        if variavel.isnumeric():
            numero = int(variavel)
            return numero
        if variavel.replace('.', '', 1).isdigit():
            numero = float(variavel)
            return numero
        else:
            print(f'ERRO! \'{variavel}\' NÃO É VALIDO. Digite um número valido')
