def leia_dinheiro(msg):
    while True:
        variavel = str(input(msg)).replace(',', '.').strip()
        if variavel.isnumeric():
            return int(variavel)
        if variavel.replace('.', '', 1).isdigit():
            return float(variavel)
        else:
            print(f'ERRO! \'{variavel}\' NÃO É VALIDO. Digite um número valido')

