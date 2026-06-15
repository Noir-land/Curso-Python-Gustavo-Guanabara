
"""
Adapte o código do desafio 107, criando uma função adicional chamada 'moeda()' que consiga mostrar os valores como um valor monetário formatado.
"""


import  Moeda


valor = int(input('Digite um valor: '))
cabecalho.titulo('-=')
print(f'O dobro de {Moeda.moeda(valor)} é {Moeda.moeda(Moeda.aumentar(valor))}')
print(f'O {Moeda.moeda(valor)} menos {valor} é {Moeda.moeda(Moeda.diminuir(valor))}')
print(f'A metade de {Moeda.moeda(valor) } é {Moeda.moeda(Moeda.dividir(valor))}')
print(f'10% de {Moeda.moeda(valor)} é {Moeda.moeda(Moeda.porcento(valor, 10))}')
print(f'O valor {Moeda.moeda(valor)} com menos 19% é {Moeda.moeda(Moeda.menos_porcento(valor, 19))}')
cabecalho.titulo('-=')
