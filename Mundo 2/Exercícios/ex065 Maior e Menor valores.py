"""
Crie um programa que leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
"""

num = soma = cont = div = maior = menor = 0
pergunta = 'S'
while pergunta in "sS":
    num = int(input("Digite um numero: "))
    soma += num
    cont += 1
    div = soma / cont
    if cont == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    pergunta = str(input("deseja continuar?[N/S] "))
print(
    f"Foram digitados {cont} numeros e sua soma foi de {soma} "
    f"e a media deles é {div}"
)
print(f"O  menor foi {menor} ")
print(f"O  maior foi {maior} ")
