"""
Crie um programa que vai ler vários números e colocá-los em uma lista
Depois disso, mostre:
quantos números foram digitados.
a lista de valores, ordenada de forma decrescente
se o valor 5 foi digitado e está ou não na lista.
"""

Lista = list()
while True:
    Lista.append(int(input('Digite um numero: ')))
    resposta = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if resposta in "N":
        break
Lista.sort(reverse=True)
print(f'Você digitou {len(Lista)} números.')
print(f'A Listade numeros em ordem decescente foi', end=' ')
for n in Lista:
    print(f'{n}', end=' ')
if 5 in Lista:
    print('\nO número cinco existe nesta lista.')
else:
    print('\nO número cinco não existe nesta lista.')
