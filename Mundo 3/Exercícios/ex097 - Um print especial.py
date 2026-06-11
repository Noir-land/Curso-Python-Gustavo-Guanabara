"""Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro 
e mostre uma mensagem com tamanho adaptável.

Ex:
escreva("Olá, Mundo!")

Saída:

~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
"""

def cabecalho(titulo):
    tmh = len(titulo)
    print('-=' * len(titulo))
    print(f'{titulo:^{tmh * 2}}')
    print('--'*len(titulo))


cabecalho('Olá, MUNDO')
cabecalho('Pessimismo leva à fraqueza, otimismo ao pode')
cabecalho('oi')