n1 = int(input("Digite um numero: "))
n2 = int(input("digite um numero: "))
maior = n1
op = 0
while op != 5:
    op = int(input('''\n[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR
Digite o numero da opção: '''))
    if op == 1:
        print(f"O resultado da soma de  {n1} + {n2} = {n1+n2} ")
    elif op == 2:
        print(f"O resultado da multiplicação de {n1} x {n2} = {n1*n2}")
    elif op == 3:
        if n2 > n1:
            maior = n2
        print(f"Dentre os numeros {n1} e {n2} o maior é {maior}")
    elif op == 4:
        print("Digite os novos numeros")
        n1 = int(input("Digite um numero: "))
        n2 = int(input("digite um numero: "))
    elif op == 5:
        print("fechando...")
    else:
        print("invalido")
print("Finalizado")
