"""
Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
A média de idade do grupo
Qual é o nome do homem mais velho
Quantas mulheres têm menos de 20 anos
 """


soma = 0
midade = 0
hvelho = ''
m = 0
for p in range(1, 3):
    print(f'----{p}º PESSOA-----')
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo(F/M)")).strip()
    soma += idade
    media = soma / p
    if p == 1 and sexo in "Mm":
        midade = idade
        hvelho = nome
    if sexo in "Mm" and idade > midade:
        midade = idade
        hvelho = nome
    if sexo in "Ff" and idade < 20:
        m += 1
print(f"A media de idade do grupo é {media}")
print(f"O homen mais velho tem {midade} anos e seu nome é {hvelho}")
print(f"Ao todo são {m} mulheres menores que 20 anos")
