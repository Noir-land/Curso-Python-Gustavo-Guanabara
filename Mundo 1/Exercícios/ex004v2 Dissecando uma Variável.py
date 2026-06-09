"""
Faça um programa que leia algo pelo teclado 
e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele
"""

a = input('Digite algo: ')
print('É um numero interiro ? ', a.isnumeric())
print('Tem letra ? ', a.isalpha())
print('Conntem numero e letra ? ', a.isalnum())
print('Contem letras maiuscula é minuscula ? ', a.istitle())
print('Contem somente espaços ? ', a.isspace())
print("É um numero decimal ? ", a.isdecimal())
print('É imprimivel ? ', a.isprintable())
