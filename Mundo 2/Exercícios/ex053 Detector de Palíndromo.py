""" 
Crie um programa que leia uma frase qualquer
E diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos:
Após a sopa
A sacada da casa
A torre da derrota
o lobo ama o bolo
Anotaram a data da maratona
"""

frase = str(input("Digite uma frase: ")).strip().upper()
dividir = frase.split()
junto = ''.join(dividir)
inverso = ''
for letras in range(len(junto)-1, -1, -1):
    inverso += junto[letras]
if inverso == junto:
    print("TEMOS UM POLINDRAMO")
else:
    print("NÃO É UM POLINDRAMO")
