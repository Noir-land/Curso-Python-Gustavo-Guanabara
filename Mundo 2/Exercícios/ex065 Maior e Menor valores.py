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
