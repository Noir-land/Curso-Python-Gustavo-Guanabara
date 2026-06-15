import  Moeda

valor = int(input('Digite um valor: '))
print()
print(f'O dobro de {Moeda.moeda(valor)} é {Moeda.aumentar(valor, True)}')
print(f'O {Moeda.moeda(valor)} menos {valor} é {Moeda.diminuir(valor, True)}')
print(f'A metade de {Moeda.moeda(valor) } é {Moeda.dividir(valor, True)}')
print(f'10% de {Moeda.moeda(valor)} é {Moeda.porcento(valor, 10, True)}')
print(f'O valor {Moeda.moeda(valor)} com menos 19% é {Moeda.menos_porcento(valor, 19, True)}')
