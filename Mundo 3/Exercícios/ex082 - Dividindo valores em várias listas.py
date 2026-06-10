"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

Lista = list()
ListaPar = list()
ListaImpar = list()
while True:
    Lista.append(int(input('Digite um numero: ')))
    resposta = str(input('Deseja continuar?[S/N] ')).upper().strip()
    if resposta == 'N':
        break
for i, n in enumerate(Lista):
    if n % 2 == 0:
        ListaPar.append(n)
    else:
        ListaImpar.append(n)

print(f'A lista de números é {Lista}')
print(f'Os números pares são {ListaPar}')
print(f'Os números imperes são {ListaImpar}')
