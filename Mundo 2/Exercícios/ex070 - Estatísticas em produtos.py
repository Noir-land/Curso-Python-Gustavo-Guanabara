"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato
"""

print("*"*40)
print('{:^40}'.format("NOIR SUPERMERCADO"))
print("*"*40)
opção = b = " "
vm = menor = maior = cont = total = menorpre = maiorpre = 0
while True:
    produto = str(input("Nome do produto: "))
    valor = float(input("Valor do produto em R$: "))
    opção = str(input("DESEJA CONTINUAR ? (S/N)")).strip().upper()[0]
    total += valor
    cont += 1
    while opção not in 'SN':
        opção = str(input("DESEJA CONTINUAR ? (S/N)")).strip().upper()[0]
    if valor >= 1000:
        vm += 1
    if cont == 1:
        menor = valor
        maior = valor
        menorpre = produto
        maiorpre = produto
    else:
        if valor < menor:
            menor = valor
            menorpre = produto
        if valor > maior:
            maior = valor
            maiorpre = produto
    if opção == "N":
        break
print(f"As compras realizadas teram um total de R$ {total:.2f}\nExistem {vm} produtos acima de R$ 1000.00.")
print(f"O produto com o menor valor foi {menorpre} e custou R${menor:.2f}")
print(f"o produto com maior valor foi {maiorpre} e custou R${maior:.2f}")
