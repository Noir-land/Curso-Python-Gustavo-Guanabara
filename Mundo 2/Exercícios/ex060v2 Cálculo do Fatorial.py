n = int(input("Digite um numero para obeter o factorial. "))
f = 1
print(f'{n}! = ', end='')
for c in range(n, 0, -1):
    print(f'{c}', end="")
    print(" x " if c > 1 else " = ", end='')
    f *= c
print(f)
