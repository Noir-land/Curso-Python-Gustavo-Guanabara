"""
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla.
No final, mostre:
quantas vezes apareceu o valor 9
em que posição foi digitado o primeiro valor 3
quais foram os números pares
"""

# num1 = int(input("digite o primeiro numero"))
# num2 = int(input("digite o segundo numero"))
# num3 = int(input("digite o terceiro numero"))
# num4 = int(input("digite o ultimo numero"))
# NumTupla = num1, num2, num3, num4
NumTupla = (int(input('Digite o primeiro número: ')),
            int(input('Digite o segundo  número: ')),
            int(input('Digite o terceiro número: ')),
            int(input('Digite o ultimo   número: ')),)
print(type(NumTupla))
print(f'Os numeros {NumTupla} foram digitados')
print(f"O número 9 apareceu {NumTupla.count(9)}ª vezes")
if 3 in NumTupla:
    print(f"O numero 3 apareceu na {NumTupla.index(3)+1} posição")
else:
    print("O numero 3 não aparece em nenhuma posição")
print("Os numeros pares são:", end=' ')
for n in NumTupla:
    if n % 2 == 0:
        print(n, end=' ')
