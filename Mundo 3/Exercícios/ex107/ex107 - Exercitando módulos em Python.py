from utilitariosCV_exercicio_110 import Moeda, cabecalho


valor = int(input('Digite um valor: '))
cabecalho('-=')
print(f'O dobro de {valor} é {Moeda.aumentar(valor)}')
print(f'O {valor} menos {valor} é {Moeda.diminuir(valor)}')
print(f'A metade de {valor} é {Moeda.dividir(valor)}')
print(f'10% de {valor} é {Moeda.porcento(valor, 10)}')
print(f'O valor {valor} com menos 19% é {Moeda.menos_porcento(valor, 19)}')
cabecalho('-=')
