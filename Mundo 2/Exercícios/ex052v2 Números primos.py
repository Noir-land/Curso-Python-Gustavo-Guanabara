num = int(input("Digite um numero: "))
for c in range(1, num + 1):
    if num % c == 0:
        print(f"\nDi {c} ", end=" ")
    else:
        print(f"Na {c}", end=" ")
