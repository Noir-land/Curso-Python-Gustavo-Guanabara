sequence = int(input("Digite quantas sequecias iram aparecer: "))
num = 0
num2 = 1
print(f"{num} > {num2}", end=' ')
cont = 3
while cont <= sequence:
    num3 = num + num2
    print(f"> {num3}", end=' ')
    num = num2
    num2 = num3
    cont += 1

print("fim")
