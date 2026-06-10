"""
Crie um programa que vai ler vários números e colocá-los em uma lista
Depois disso, mostre:
quantos números foram digitados.
a lista de valores, ordenada de forma decrescente
se o valor 5 foi digitado e está ou não na lista.
"""

Lista = list()
Loop = True
contador = 0
numerocinco = None
while Loop:
    numero = int(input('Digite um numero: '))
    resposta = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if resposta in "N":
        Loop = False
    if numero == 5:
        numerocinco = 'O número cinco existe nesta lista.'
    else:
        numerocinco = 'O número cinco não existe nesta lista.'
    if contador <= 0:
        Lista.append(numero)
    else:
        if numero > Lista[0]:
            Lista.insert(0, numero)
        elif numero < Lista[-1]:
            Lista.append(numero)
        else:
            for i in Lista:
                Lista.insert(i, numero)
                break
    contador += 1
print(f'Você digitou {len(Lista)} números.')
print(f'A Listade numeros em ordem decescente foi', end=' ')
for n in Lista:
    print(f'{n}', end=' ')
print(f'\n{numerocinco}', end='\n')
