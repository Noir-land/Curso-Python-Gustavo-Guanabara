print("*"*40)
print('{:^40}'.format("NOIR SUPERMERCADO"))
print("*"*40)
opção = b = " "
vm = menor = maior = cont = total = menorpre = maiorpre = produtos = 0
while True:
    produto = str(input("Nome do produto: "))
    valor = float(input("Valor do produto em R$: "))
    opção = str(input("DESEJA CONTINUAR ? (S/N)")).strip().upper()[0]
    total += valor
    cont += 1
    while opção not in 'SN':
        opção = str(input("DESEJA CONTINUAR ? (S/N)")).strip().upper()[0]
    if valor >= 1000:
        produtos += 1
        vm = produtos
        vm = (f"Existem {vm} produtos")
        if vm == 1:
            vm = (f"Existem {vm} produto")
    if vm == 0:
        vm = 'Não existem produtos'
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
print(f"As compras realizadas teram um total de R$ {total:.2f}\n{vm} acima de R$ 1000.00.")
print(f"O produto com o menor valor foi {menorpre} e custou R${menor:.2f}")
print(f"o produto com maior valor foi {maiorpre} e custou R${maior:.2f}")
